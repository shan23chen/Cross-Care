import json
import os
import re
import pandas as pd
from collections import defaultdict
from multiprocessing import Pool, cpu_count
from functools import partial


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


def remove_latex_commands(s):
    """
    Remove LaTeX commands from a string.

    Parameters:
        s (str): The input string.

    Returns:
        str: The string with LaTeX commands removed.
    """
    s = re.sub(r"\\[nrt]|[\n\r\t]", " ", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = re.sub(r"\\.", "", s)
    s = re.sub(r"\\begin\{.*?\}.*?\\end\{.*?\}", "", s, flags=re.DOTALL)
    s = re.sub(r"\$.*?\$", "", s)
    s = re.sub(r"\\[.*?\\]", "", s)
    s = re.sub(r"\\\(.*?\\\)", "", s)
    s = re.sub(r"\\\[.*?\\\]", "", s)
    s = re.sub(r"(?<=\W)\\|\\(?=\W)", "", s)
    return s.strip()


def process_file(
    file_path,
    medical_patterns,
    racial_patterns,
    gender_patterns,
    drug_patterns,
    cancer_patterns,
    metadata_keys,
    remove_latex,
):
    """
    Process a single JSONL file to extract relevant data.

    Parameters:
        file_path (str): Path to the JSONL file.
        medical_patterns (dict): Dictionary of compiled regex patterns for medical keywords.
        racial_patterns (dict): Dictionary of compiled regex patterns for racial keywords.
        gender_patterns (dict): Dictionary of compiled regex patterns for gender keywords.
        metadata_keys (list of str): List of metadata keys to extract.
        remove_latex (bool): Whether to remove LaTeX commands from the text.

    Returns:
        tuple: A tuple containing:
            - output_data (list of dict): Extracted data.
            - total_texts (int): Total number of texts processed.
    """

    output_data = []
    total_texts = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            total_texts += 1
            try:
                entry = json.loads(line)
                text = entry["text"]
                if remove_latex:
                    text = remove_latex_commands(text)
                meta_data = entry.get("meta", {})

                # Check if the text contains a medical keyword
                if any(pattern.search(text) for pattern in medical_patterns.values()):
                    row_data = defaultdict(int)
                    row_data["text"] = text

                    for key in metadata_keys:
                        row_data[key] = meta_data.get(key, None)

                    for patterns in [
                        medical_patterns,
                        racial_patterns,
                        gender_patterns,
                        drug_patterns,
                        cancer_patterns,
                    ]:
                        for key, pattern in patterns.items():
                            row_data[key] = len(pattern.findall(text))

                    output_data.append(row_data)

            except json.JSONDecodeError as e:
                print(f"Error loading line in {file_path}: {line}. Error: {e}")

    return output_data, total_texts


def jsonl_folder_filtering(
    input_folder_path,
    medical_dict,
    racial_dict,
    gender_dict,
    drug_dict,
    cancer_dict,
    metadata_keys=[],
    output_folder_path=None,
    remove_latex=True,
    save_file=True,
    filename="filtered_data.json",
    total_texts_filename="total_texts.txt",
):
    """
    Filter and process all JSONL files in a folder.

    Parameters:
        input_folder_path (str): Path to the folder containing JSONL files.
        medical_dict (dict): Dictionary of medical keywords.
        racial_dict (dict): Dictionary of racial keywords.
        gender_dict (dict): Dictionary of gender keywords.
        drug_dict (dict): Dictionary of drug keywords.
        cancer_dict (dict): Dictionary of cancer keywords.
        metadata_keys (list of str): List of metadata keys to extract.
        output_folder_path (str): Path to the folder where output should be saved.
        remove_latex (bool): Whether to remove LaTeX commands from the text.
        save_file (bool): Whether to save the output data to a file.
        filename (str): Name of the output file.
        total_texts_filename (str): Name of the file to save the total number of texts.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted data.
    """

    medical_patterns = {k: create_keyword_pattern(v) for k, v in medical_dict.items()}
    racial_patterns = {k: create_keyword_pattern(v) for k, v in racial_dict.items()}
    gender_patterns = {k: create_keyword_pattern(v) for k, v in gender_dict.items()}
    drug_patterns = {k: create_keyword_pattern(v) for k, v in drug_dict.items()}
    cancer_patterns = {k: create_keyword_pattern(v) for k, v in cancer_dict.items()}

    file_paths = [
        os.path.join(input_folder_path, file_name)
        for file_name in os.listdir(input_folder_path)
        if file_name.endswith(".jsonl")
    ]

    with Pool(cpu_count()) as p:
        results = p.starmap(
            process_file,
            [
                (
                    file_path,
                    medical_patterns,
                    racial_patterns,
                    gender_patterns,
                    drug_patterns,
                    cancer_patterns,
                    metadata_keys,
                    remove_latex,
                )
                for file_path in file_paths
            ],
        )

    output_data = [item for sublist, _ in results for item in sublist]
    total_texts = sum(total for _, total in results)

    # Save the total number of texts to a txt file
    if output_folder_path is not None:
        with open(os.path.join(output_folder_path, total_texts_filename), "w") as f:
            f.write(str(total_texts))

    df_output = pd.DataFrame(output_data)
    print(df_output.shape)

    all_keyword_columns = (
        list(medical_patterns.keys())
        + list(racial_patterns.keys())
        + list(gender_patterns.keys())
        + list(drug_patterns.keys())
        + list(cancer_patterns.keys())
    )

    for col in all_keyword_columns:
        if col in df_output.columns:
            df_output[col] = df_output[col].fillna(0).astype(int)

    # Assigning a unique text_id for each unique text
    df_output["text_id"] = pd.factorize(df_output["text"])[0]

    column_order = ["text", "text_id"] + metadata_keys + all_keyword_columns
    df_output = df_output[column_order]

    if save_file:
        if output_folder_path is not None:
            os.makedirs(output_folder_path, exist_ok=True)
            output_path = os.path.join(output_folder_path, filename)
            df_output.to_csv(output_path, index=False)  # Save as CSV
        else:
            print(
                "Warning: Output folder path is not provided. The DataFrame is not saved to a file."
            )

    return df_output


def process_chunk(
    chunk,
    medical_patterns,
    racial_patterns,
    gender_patterns,
    drug_patterns,
    cancer_patterns,
    metadata_keys,
    remove_latex,
):
    output_data = []
    total_texts = 0

    for line in chunk:
        total_texts += 1
        try:
            entry = json.loads(line)
            text = entry["text"]
            if remove_latex:
                text = remove_latex_commands(text)
            meta_data = entry.get("meta", {})

            # Check if the text contains a medical keyword
            if any(pattern.search(text) for pattern in medical_patterns.values()):
                row_data = defaultdict(int)
                row_data["text"] = text

                for key in metadata_keys:
                    row_data[key] = meta_data.get(key, None)

                for patterns in [
                    medical_patterns,
                    racial_patterns,
                    gender_patterns,
                    drug_patterns,
                    cancer_patterns,
                ]:
                    for key, pattern in patterns.items():
                        row_data[key] = len(pattern.findall(text))

                output_data.append(row_data)

        except json.JSONDecodeError as e:
            print(f"Error loading line: {line}. Error: {e}")

    return output_data, total_texts


def jsonl_single_file_filtering(
    file_path,
    medical_dict,
    racial_dict,
    gender_dict,
    drug_dict,
    cancer_dict,
    metadata_keys=[],
    output_folder_path=None,
    remove_latex=True,
    save_file=True,
    filename="filtered_data.json",
    total_texts_filename="total_texts.txt",
):
    medical_patterns = {k: create_keyword_pattern(v) for k, v in medical_dict.items()}
    racial_patterns = {k: create_keyword_pattern(v) for k, v in racial_dict.items()}
    gender_patterns = {k: create_keyword_pattern(v) for k, v in gender_dict.items()}
    drug_patterns = {k: create_keyword_pattern(v) for k, v in drug_dict.items()}
    cancer_patterns = {k: create_keyword_pattern(v) for k, v in cancer_dict.items()}

    with open(file_path, "r") as file:
        lines = file.readlines()

    num_cores = cpu_count()
    chunk_size = len(lines) // num_cores
    if len(lines) % num_cores != 0:
        num_cores += 1
    print(f"Using {num_cores} cores")
    print(f"Chunk size: {chunk_size}")
    print(f"Total lines: {len(lines)}")

    chunks = [lines[i : i + chunk_size] for i in range(0, len(lines), chunk_size)]

    with Pool(num_cores) as p:
        results = p.map(
            partial(
                process_chunk,
                medical_patterns=medical_patterns,
                racial_patterns=racial_patterns,
                gender_patterns=gender_patterns,
                drug_patterns=drug_patterns,
                cancer_patterns=cancer_patterns,
                metadata_keys=metadata_keys,
                remove_latex=remove_latex,
            ),
            chunks,
        )

    output_data = [item for sublist, _ in results for item in sublist]
    total_texts = sum(total for _, total in results)

    # Save the total number of texts to a txt file
    if output_folder_path is not None:
        with open(os.path.join(output_folder_path, total_texts_filename), "w") as f:
            f.write(str(total_texts))

    df_output = pd.DataFrame(output_data)

    all_keyword_columns = (
        list(medical_patterns.keys())
        + list(racial_patterns.keys())
        + list(gender_patterns.keys())
        + list(drug_patterns.keys())
        + list(cancer_patterns.keys())
    )
    for col in all_keyword_columns:
        if col not in df_output.columns:
            df_output[col] = 0

    df_output[all_keyword_columns] = (
        df_output[all_keyword_columns].fillna(0).astype(int)
    )

    # Assigning a unique text_id for each unique text
    df_output["text_id"] = pd.factorize(df_output["text"])[0]

    column_order = ["text", "text_id"] + metadata_keys + all_keyword_columns
    df_output = df_output[column_order]

    if save_file:
        if output_folder_path is not None:
            os.makedirs(output_folder_path, exist_ok=True)
            output_path = os.path.join(output_folder_path, filename)
            df_output.to_csv(output_path, index=False)  # Save as CSV
        else:
            print(
                "Warning: Output folder path is not provided. The DataFrame is not saved to a file."
            )

    return df_output
