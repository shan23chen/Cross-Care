import json
import pandas as pd
from collections import defaultdict
from multiprocessing import Pool, cpu_count
from functools import partial
import re
import os
from tqdm import tqdm


def create_keyword_pattern(keywords):
    """
    Create a regex pattern for keyword matching.

    Parameters:
        keywords (list of str): A list of keywords to create a pattern for.

    Returns:
        re.Pattern: A compiled regex pattern that matches any of the provided keywords.
    """
    pattern = r"(?:(?<=\W)|(?<=^))(" + "|".join(map(re.escape, keywords)) + r")(?=\W|$)"
    return re.compile(pattern, re.IGNORECASE)


def co_occurrence_within_window(
    data, medical_dict, racial_dict, gender_dict, drug_dict, window_size, aggregate=True
):
    """
    Calculate co-occurrences of medical terms with racial and gender terms within a specified window of words.

    Args:
        data (list of str): List of documents to process.
        medical_dict (dict): Dictionary of medical keywords categorized by some keys.
        racial_dict (dict): Dictionary of racial keywords categorized by some keys.
        gender_dict (dict): Dictionary of gender keywords categorized by some keys.
        drug_dict (dict): Dictionary of drug keywords categorized by some keys.
        window_size (int): Number of words to consider around the medical term match.
        aggregate (bool): If True, aggregates matches by category keys. If False, keeps individual term matches.

    Returns:
        df_racial (DataFrame): DataFrame containing co-occurrences with racial terms.
        df_gender (DataFrame): DataFrame containing co-occurrences with gender terms.
        df_drug (DataFrame): DataFrame containing co-occurrences with drug terms.
    """
    co_occurrences_racial = defaultdict(lambda: defaultdict(int))
    co_occurrences_gender = defaultdict(lambda: defaultdict(int))
    co_occurrences_drug = defaultdict(lambda: defaultdict(int))

    medical_patterns = {k: create_keyword_pattern(v) for k, v in medical_dict.items()}
    racial_patterns = {k: create_keyword_pattern(v) for k, v in racial_dict.items()}
    gender_patterns = {k: create_keyword_pattern(v) for k, v in gender_dict.items()}
    drug_patterns = {k: create_keyword_pattern(v) for k, v in drug_dict.items()}

    for text in tqdm(data, desc="Processing documents"):
        for med_key, med_pattern in medical_patterns.items():
            for med_match in med_pattern.finditer(text):
                start_pos = med_match.start()
                end_pos = med_match.end()

                # Get the words in the context window around the match
                words = text.split()
                start_word_pos = len(text[:start_pos].split()) - 1
                end_word_pos = len(text[:end_pos].split())
                context_words = words[
                    max(0, start_word_pos - window_size) : min(
                        len(words), end_word_pos + window_size
                    )
                ]
                context_str = " ".join(context_words)

                # Check context for racial terms
                for race_key, race_pattern in racial_patterns.items():
                    for race_match in race_pattern.finditer(context_str):
                        co_occurrences_racial[
                            med_key if aggregate else med_match.group()
                        ][race_key if aggregate else race_match.group()] += 1

                # Check context for gender terms
                for gender_key, gender_pattern in gender_patterns.items():
                    for gender_match in gender_pattern.finditer(context_str):
                        co_occurrences_gender[
                            med_key if aggregate else med_match.group()
                        ][gender_key if aggregate else gender_match.group()] += 1

                # Check context for drug terms
                for drug_key, drug_pattern in drug_patterns.items():
                    for drug_match in drug_pattern.finditer(context_str):
                        co_occurrences_drug[
                            med_key if aggregate else med_match.group()
                        ][drug_key if aggregate else drug_match.group()] += 1

    # Ensure all combinations are present
    if aggregate:
        for med_key in medical_patterns.keys():
            for race_key in racial_patterns.keys():
                co_occurrences_racial[med_key][race_key] += 0
            for gender_key in gender_patterns.keys():
                co_occurrences_gender[med_key][gender_key] += 0
            for drug_key in drug_patterns.keys():
                co_occurrences_drug[med_key][drug_key] += 0
    else:
        for med_key, med_keywords in medical_dict.items():
            for med_keyword in med_keywords:
                for race_key, race_keywords in racial_dict.items():
                    for race_keyword in race_keywords:
                        co_occurrences_racial[med_keyword][race_keyword] += 0
                for gender_key, gender_keywords in gender_dict.items():
                    for gender_keyword in gender_keywords:
                        co_occurrences_gender[med_keyword][gender_keyword] += 0
                for drug_key, drug_keywords in drug_dict.items():
                    for drug_keyword in drug_keywords:
                        co_occurrences_drug[med_keyword][drug_keyword] += 0

    # Convert co_occurrences dictionaries to dataframes
    df_racial = pd.DataFrame(co_occurrences_racial).fillna(0).astype(int).T
    df_gender = pd.DataFrame(co_occurrences_gender).fillna(0).astype(int).T
    df_drug = pd.DataFrame(co_occurrences_drug).fillna(0).astype(int).T

    return df_racial, df_gender, df_drug


def calculate_disease_by_group(
    stack_dataframe, medical_dict, gender_dict, racial_dict, drug_dict
):
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


def calculate_subgroup_disease_counts_by_date(
    df_output, medical_dict, gender_dict, racial_dict, drug_dict, grouping_column
):
    # Initialize DataFrames to store results
    gender_counts_by_date = pd.DataFrame()
    race_counts_by_date = pd.DataFrame()
    drug_counts_by_date = pd.DataFrame()

    # Group by date
    for date, group_df in df_output.groupby(grouping_column):
        # Calculate the co-occurrences for the subgroup within this date group
        (
            disease_gender_counts,
            disease_race_counts,
            disease_drug_counts,
        ) = calculate_disease_by_group(
            group_df, medical_dict, gender_dict, racial_dict, drug_dict
        )

        # Add the date information
        disease_gender_counts[grouping_column] = date
        disease_race_counts[grouping_column] = date
        disease_drug_counts[grouping_column] = date

        # Append the results
        gender_counts_by_date = pd.concat(
            [gender_counts_by_date, disease_gender_counts]
        )
        race_counts_by_date = pd.concat([race_counts_by_date, disease_race_counts])
        drug_counts_by_date = pd.concat([drug_counts_by_date, disease_drug_counts])

    # Reset index and return
    return (
        gender_counts_by_date.reset_index(),
        race_counts_by_date.reset_index(),
        drug_counts_by_date.reset_index(),
    )


def analyze_data_co_occurrence(
    source_name, data_path, medical_dict, racial_dict, gender_dict, drug_dict
):
    df_output = pd.read_csv(data_path)

    output_dir = f"output_{source_name}"
    # output_dir = f"output_{source_name}_cancer"
    os.makedirs(output_dir, exist_ok=True)

    print("output_dir", output_dir)

    total_disease_counts = df_output[list(medical_dict.keys())].sum()
    total_disease_counts.to_csv(os.path.join(output_dir, "total_disease_counts.csv"))

    # Conditional grouping based on source_name
    if source_name == "books":
        grouping_column = "publication_date"
    else:
        grouping_column = "timestamp"

    disease_date_counts = (
        df_output.groupby(grouping_column)[list(medical_dict.keys())]
        .sum()
        .reset_index()
    )
    disease_date_counts.to_csv(os.path.join(output_dir, "disease_date_counts.csv"))

    # 3: Disease Mention Counts with Each Race
    (
        disease_gender_counts,
        disease_race_counts,
        disease_drug_counts,
    ) = calculate_disease_by_group(
        df_output, medical_dict, gender_dict, racial_dict, drug_dict
    )

    disease_race_counts.to_csv(os.path.join(output_dir, "disease_race_counts.csv"))

    # 4: Disease Mention Counts with Each Gender
    disease_gender_counts.to_csv(os.path.join(output_dir, "disease_gender_counts.csv"))

    # 5: Disease Mention Counts with Each Drug
    disease_drug_counts.to_csv(os.path.join(output_dir, "disease_drug_counts.csv"))

    # 6: Disease Mention Counts for subgroups across time
    (
        gender_counts_by_date,
        race_counts_by_date,
        drug_counts_by_date,
    ) = calculate_subgroup_disease_counts_by_date(
        df_output, medical_dict, gender_dict, racial_dict, drug_dict, grouping_column
    )

    gender_counts_by_date.to_csv(os.path.join(output_dir, "gender_counts_by_date.csv"))
    race_counts_by_date.to_csv(os.path.join(output_dir, "race_counts_by_date.csv"))
    drug_counts_by_date.to_csv(os.path.join(output_dir, "drug_counts_by_date.csv"))

    # Co-occurrence within window sizes
    data = df_output["text"].tolist()
    window_sizes = [10, 50, 100, 250]

    for window in window_sizes:
        df_racial, df_gender, df_drug = co_occurrence_within_window(
            data,
            medical_dict,
            racial_dict,
            gender_dict,
            drug_dict,
            window,
            aggregate=True,
        )

        window_dir = os.path.join(output_dir, f"window_{window}")
        os.makedirs(window_dir, exist_ok=True)

        df_racial.to_csv(os.path.join(window_dir, "co_occurrence_racial.csv"))
        df_gender.to_csv(os.path.join(window_dir, "co_occurrence_gender.csv"))
        df_drug.to_csv(os.path.join(window_dir, "co_occurrence_drug.csv"))
