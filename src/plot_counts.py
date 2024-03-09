import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("/home/wsl_legion/Cross-Care/")
from dicts.dict_medical import medical_keywords_dict
from dicts.dict_census_est import census_dict


#### Helper functions ####


# Code to Disease
def replace_disease_codes(df, medical_keywords_dict):
    """
    Replace disease codes with names in a DataFrame.

    :param df: DataFrame with disease names/codes.
    :param code_to_name_dict: Dictionary mapping codes to lists of names.
    :return: DataFrame with updated disease names.
    """
    for index, row in df.iterrows():
        disease = row["disease"]
        # Check if the last two characters are '.0'
        if isinstance(disease, str) and disease.endswith(".0"):
            # Lookup the code in the dictionary and get the first name
            name_list = medical_keywords_dict.get(disease)
            if name_list:
                df.at[index, "disease"] = name_list[0]
    return df


def calculate_percentage_deviation(df, group_columns, census_dict):
    # Calculate the total counts
    total_counts = df[group_columns].sum(axis=1).to_numpy()

    # Prepare expected counts based on census percentages
    expected_counts = np.array(
        [total_counts * (census_dict[group] / 100) for group in group_columns]
    ).T

    # Calculate percentage deviation
    percentage_deviation = (
        (df[group_columns].to_numpy() - expected_counts) / expected_counts
    ) * 100
    return pd.DataFrame(percentage_deviation, columns=group_columns)


#### Plotting functions ####


# plot total counts for a disease
def plot_total_counts(csv_path, medical_keywords_dict, plot_dir, plot_name):
    df = pd.read_csv(csv_path)
    df = df.rename(columns={"Unnamed: 0": "disease"})
    df = replace_disease_codes(df, medical_keywords_dict)
    df = df.sort_values(by=df.columns[1], ascending=False)

    # Debug take top 20
    df = df.head(20)

    plt.figure(figsize=(10, 6))
    plt.bar(df["disease"], df[df.columns[1]])
    plt.xlabel("Disease")
    plt.ylabel("Total Counts")
    plt.title("Total Disease Counts")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/{plot_name}.png")
    plt.close()


# Calculate subgroup counts
def plot_subgroup_counts(csv_path, medical_keywords_dict, plot_dir, plot_name, groups):
    df = pd.read_csv(csv_path)
    df = df.rename(columns={"Unnamed: 0": "disease"})
    df = replace_disease_codes(df, medical_keywords_dict)

    # Debug take top 20
    df = df.head(20)

    plt.figure(figsize=(10, 6))
    bar_width = 0.15
    for i, group in enumerate(groups):
        plt.bar(
            [x + bar_width * i for x in range(len(df))],
            df[group],
            bar_width,
            label=group,
        )

    plt.xlabel("Disease")
    plt.ylabel("Counts")
    plt.title("Disease Counts by Subgroup")
    plt.xticks(range(len(df)), df["disease"], rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/{plot_name}.png")
    plt.close()


# Calculate percentage deviation
def plot_percentage_difference(
    csv_path, medical_keywords_dict, plot_dir, plot_name, groups, census_dict
):
    df = pd.read_csv(csv_path)
    df = df.rename(columns={"Unnamed: 0": "disease"})
    df = replace_disease_codes(df, medical_keywords_dict)

    # Debug take top 20
    df = df.head(20)

    percentage_deviation_df = calculate_percentage_deviation(df, groups, census_dict)

    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    for i, group in enumerate(groups):
        plt.bar(
            [x + bar_width * i for x in range(len(df))],
            percentage_deviation_df[group],
            bar_width,
            label=group,
        )

    plt.xlabel("Disease")
    plt.ylabel("Percentage Deviation")
    plt.title("Percentage Deviation by Subgroup")
    plt.xticks(range(len(df)), df["disease"], rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/{plot_name}.png")
    plt.close()


#### Main ####

if __name__ == "__main__":
    # paths
    count_dir = "output_arxiv"
    plot_dir = "plots/arxiv"

    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)

    # window sizes
    window_sizes = [10, 50, 100, 250]
    demo_cat = ["gender", "racial"]

    # Plot total counts
    plot_total_counts(
        csv_path=f"{count_dir}/total_disease_counts.csv",
        medical_keywords_dict=medical_keywords_dict,
        plot_dir=plot_dir,
        plot_name="total_disease_counts",
    )
    print("Plotted total disease counts.")

    for window_size in window_sizes:
        for demo in demo_cat:
            filename = f"{count_dir}/window_{window_size}/co_occurrence_{demo}.csv"

            # read csv
            df = pd.read_csv(
                filename, skiprows=1, header=None, names=["disease", "gender", "count"]
            )
            pivot_df = df.pivot_table(
                index="disease",
                columns="gender",
                values="count",
                aggfunc="sum",
                fill_value=0,
            ).reset_index()
            pivot_df.columns.name = None
            pivot_df = pivot_df.rename(columns={"male": "male", "female": "female"})
            pivot_df = pivot_df[["disease", "male", "female"]]
            print(pivot_df.head())
            pivot_df = replace_disease_codes(pivot_df, medical_keywords_dict)

            # Prepare the data for subgroup counts plot
            if demo == "gender":
                groups = ["male", "female"]
                census_demo_dict = census_dict["gender"]
            else:  # For 'racial'
                groups = pivot_df.columns[1:]
                census_demo_dict = census_dict["racial"]

            # Plot subgroup counts
            plot_subgroup_counts(
                csv_path=filename,
                medical_keywords_dict=medical_keywords_dict,
                plot_dir=plot_dir,
                plot_name=f"window_{window_size}_{demo}_subgroup_counts",
                groups=groups,
            )
            print(f"Plotted subgroup counts for {demo}.")

            # Plot percentage difference
            plot_percentage_difference(
                csv_path=filename,
                medical_keywords_dict=medical_keywords_dict,
                plot_dir=plot_dir,
                plot_name=f"window_{window_size}_{demo}_percentage_difference",
                groups=groups,
                census_dict=census_demo_dict,
            )
            print(f"Plotted percentage difference for {demo}.")
