import os
import sys
import pandas as pd
import numpy as np
import re


def find_duplicates_in_file(file_path, list_name):
    # Read the content of the Python file
    with open(file_path, "r") as file:
        file_content = file.read()

    # Extract the list from the file content
    # This assumes the list is defined as in your example and uses 'exec'
    try:
        exec(file_content, globals())
        list_to_check = eval(list_name)
    except Exception as e:
        print(f"Error extracting list: {e}")
        return []

    # Check for duplicates
    seen = set()
    duplicates = set()
    for item in list_to_check:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)


if __name__ == "__main__":
    # Script to check
    file_path = "/home/wsl_legion/Cross-Care/keywords/keywords_cancer.py"
    list_name = "cancer_keywords"

    # check for duplicates pre processing
    duplicates = find_duplicates_in_file(file_path, list_name)
    print("Duplicate entries:", duplicates)
