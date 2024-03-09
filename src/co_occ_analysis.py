import os
import re
import pandas as pd
from collections import defaultdict
from multiprocessing import Pool, cpu_count
from functools import partial
from tqdm import tqdm


def create_keyword_pattern(keywords):
    """
    Create a regex pattern for keyword matching.
    """
    pattern = r"(?:(?<=\W)|(?<=^))(" + "|".join(map(re.escape, keywords)) + r")(?=\W|$)"
    return re.compile(pattern, re.IGNORECASE)


def find_co_occurrences(
    text, medical_patterns, racial_patterns, gender_patterns, drug_patterns, window_size
):
    """
    Find co-occurrences of terms in a given text within a specified window size.
    """
    co_occurrences = {
        "racial": defaultdict(int),
        "gender": defaultdict(int),
        "drug": defaultdict(int),
    }

    for med_key, med_pattern in medical_patterns.items():
        for med_match in med_pattern.finditer(text):
            start_pos, end_pos = med_match.span()
            words = text.split()
            start_word_pos = len(text[:start_pos].split()) - 1
            end_word_pos = len(text[:end_pos].split())
            context_words = words[
                max(0, start_word_pos - window_size) : min(
                    len(words), end_word_pos + window_size
                )
            ]
            context_str = " ".join(context_words)
           
            if med_key== "multiple myeloma":
                    print(text)
            
            for category, patterns in [
                ("racial", racial_patterns),
                ("gender", gender_patterns),
                ("drug", drug_patterns),
            ]:
                for key, pattern in patterns.items():
                    for _ in pattern.finditer(context_str):
                        co_occurrences[category][(med_key, key)] += 1
                        
    return co_occurrences


def process_texts_in_parallel(
    data, medical_dict, racial_dict, gender_dict, drug_dict, window_size
):
    """
    Process texts in parallel to find co-occurrences.
    """
    medical_patterns = {k: create_keyword_pattern(v) for k, v in medical_dict.items()}
    racial_patterns = {k: create_keyword_pattern(v) for k, v in racial_dict.items()}
    gender_patterns = {k: create_keyword_pattern(v) for k, v in gender_dict.items()}
    drug_patterns = {k: create_keyword_pattern(v) for k, v in drug_dict.items()}

    with Pool(cpu_count()) as pool:
        results = list(
            tqdm(
                pool.imap(
                    partial(
                        find_co_occurrences,
                        medical_patterns=medical_patterns,
                        racial_patterns=racial_patterns,
                        gender_patterns=gender_patterns,
                        drug_patterns=drug_patterns,
                        window_size=window_size,
                    ),
                    data,
                ),
                total=len(data),
                desc="Processing documents",
            )
        )

    # Aggregate results
    aggregated_results = {
        "racial": defaultdict(int),
        "gender": defaultdict(int),
        "drug": defaultdict(int),
    }
    for result in results:
        for category in aggregated_results:
            for key, count in result[category].items():
                aggregated_results[category][key] += 1

    return aggregated_results


def calculate_disease_by_group(
    stack_dataframe, medical_dict, gender_dict, racial_dict, drug_dict
):
    """
    Calculate disease mentions by different groups.
    """
    result_gender_df = pd.DataFrame(
        0, index=medical_dict.keys(), columns=gender_dict.keys()
    )
    result_race_df = pd.DataFrame(
        0, index=medical_dict.keys(), columns=racial_dict.keys()
    )
    result_drug_df = pd.DataFrame(
        0, index=medical_dict.keys(), columns=drug_dict.keys()
    )

    for gender in gender_dict.keys():
        result_gender_df[gender] = (
            stack_dataframe[medical_dict.keys()]
            .multiply(stack_dataframe[gender], axis=0)
            .sum()
        )

    for race in racial_dict.keys():
        result_race_df[race] = (
            stack_dataframe[medical_dict.keys()]
            .multiply(stack_dataframe[race], axis=0)
            .sum()
        )

    for drug in drug_dict.keys():
        result_drug_df[drug] = (
            stack_dataframe[medical_dict.keys()]
            .multiply(stack_dataframe[drug], axis=0)
            .sum()
        )

    return result_gender_df, result_race_df, result_drug_df


def process_date_group(args):
    date, group_df, medical_dict, gender_dict, racial_dict, drug_dict = args
    return date, calculate_disease_by_group(group_df, medical_dict, gender_dict, racial_dict, drug_dict)

def calculate_subgroup_disease_counts_by_date_parallel(df_output, medical_dict, gender_dict, racial_dict, drug_dict, grouping_column):
    # Initialize DataFrames to store results
    gender_counts_by_date = pd.DataFrame()
    race_counts_by_date = pd.DataFrame()
    drug_counts_by_date = pd.DataFrame()

    # Prepare the data for multiprocessing
    group_data = [
        (date, group, medical_dict, gender_dict, racial_dict, drug_dict)
        for date, group in df_output.groupby(grouping_column)
    ]

    # Use multiprocessing Pool to process groups in parallel
    with Pool(cpu_count()) as pool:
        results = pool.map(process_date_group, group_data)

    # Process the results
    for date, (disease_gender_counts, disease_race_counts, disease_drug_counts) in results:
        # Add the date information
        disease_gender_counts[grouping_column] = date
        disease_race_counts[grouping_column] = date
        disease_drug_counts[grouping_column] = date

        # Append the results
        gender_counts_by_date = pd.concat([gender_counts_by_date, disease_gender_counts])
        race_counts_by_date = pd.concat([race_counts_by_date, disease_race_counts])
        drug_counts_by_date = pd.concat([drug_counts_by_date, disease_drug_counts])

    # Reset index and return
    return gender_counts_by_date.reset_index(), race_counts_by_date.reset_index(), drug_counts_by_date.reset_index()


def analyze_data_co_occurrence(
    source_name,
    data_path,
    medical_dict,
    racial_dict,
    gender_dict,
    drug_dict,
    cancer_suffix="",
):
    """
    Main function to analyze data for co-occurrence.
    """
    try:
        df_output = pd.read_csv(data_path)
    except Exception as e:
        print(f"Error reading the data file: {e}")
        return

    # output_dir = f"output_{source_name}"
    output_dir = f"output_{source_name}{cancer_suffix}"
    os.makedirs(output_dir, exist_ok=True)

    total_disease_counts = df_output[list(medical_dict.keys())].sum()
    total_disease_counts.to_csv(os.path.join(output_dir, "total_disease_counts.csv"))

    grouping_column = "publication_date" if source_name == "books" else "timestamp"
    if grouping_column not in df_output.columns:
        print(f"Error: {grouping_column} column not found in the data.")
        return

    disease_date_counts = (
        df_output.groupby(grouping_column)[list(medical_dict.keys())]
        .sum()
        .reset_index()
    )
    disease_date_counts.to_csv(os.path.join(output_dir, "disease_date_counts.csv"))

    (
        disease_gender_counts,
        disease_race_counts,
        disease_drug_counts,
    ) = calculate_disease_by_group(
        df_output, medical_dict, gender_dict, racial_dict, drug_dict
    )
    disease_race_counts.to_csv(os.path.join(output_dir, "disease_race_counts.csv"))
    disease_gender_counts.to_csv(os.path.join(output_dir, "disease_gender_counts.csv"))
    disease_drug_counts.to_csv(os.path.join(output_dir, "disease_drug_counts.csv"))

#     # Disease Mention Counts for subgroups across time
#     (
#         gender_counts_by_date,
#         race_counts_by_date,
#         drug_counts_by_date,
#     ) = calculate_subgroup_disease_counts_by_date_parallel(
#         df_output, medical_dict, gender_dict, racial_dict, drug_dict, grouping_column
#     )

#     gender_counts_by_date.to_csv(os.path.join(output_dir, "gender_counts_by_date.csv"))
#     race_counts_by_date.to_csv(os.path.join(output_dir, "race_counts_by_date.csv"))
#     drug_counts_by_date.to_csv(os.path.join(output_dir, "drug_counts_by_date.csv"))

    # Windows
    data = df_output["text"].tolist()
    window_sizes = [10, 50, 100, 250]

    for window in window_sizes:
        aggregated_results = process_texts_in_parallel(
            data, medical_dict, racial_dict, gender_dict, drug_dict, window
        )
        window_dir = os.path.join(output_dir, f"window_{window}")
        os.makedirs(window_dir, exist_ok=True)

        # Convert aggregated_results to DataFrames
        for category in ["racial", "gender", "drug"]:
            df = pd.DataFrame(aggregated_results[category], index=[0]).T
            df.to_csv(os.path.join(window_dir, f"co_occurrence_{category}.csv"))


# Example usage:
# analyze_data_co_occurrence('source_name', 'data_path.csv', medical_dict, racial_dict, gender_dict, drug_dict)
