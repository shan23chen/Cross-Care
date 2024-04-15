from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import json
import os
import logging
import csv

from datetime import datetime
import calendar

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get the directory where this script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

def parse_csv(filepath):
    data = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        demographics = ['white/caucasian', 'black/african american', 'hispanic/latino', 'asian', 'native american/indigenous', 'male', 'female']
        for row in reader:
            for demo in demographics:
                if row[demo]:  # Check if the value exists
                    data.append({
                        'disease': row['disease'],
                        'count': int(row[demo].replace(",", "")),  # Remove commas and convert to int
                        'demographic': demo
                    })
    return data

def filter_by_demographic(sorted_data, demographic):
    try:
        print("Demographuic: ", demographic)
        if demographic == "gender":
            selectedDemographic = ("male", "female")
        else: 
            selectedDemographic = ('white/caucasian', 'black/african american', 'hispanic/latino', 'asian', 'native american/indigenous')
        # Define a lambda function for filtering
        filter_func = (
            lambda item: item.get("demographic", "").lower()
            in selectedDemographic
        )

        # Use the filter function with the lambda to filter the data
        filtered_data = list(filter(filter_func, sorted_data))
        return filtered_data
    except Exception as e:
        logging.error("An error occurred in filter_by_demographic:", exc_info=True)
        return []  


@app.route('/get-prevalence',  methods=["GET"])
def get_prevalence():
    category = request.args.get("category", None)
    selectedDiseases = request.args.get("selectedDiseases", None)
    
    filepath = '../data/real_prevalence.csv'
    data = parse_csv(filepath)
    
    if category:
        data = filter_by_demographic(data, category)

    if selectedDiseases != None and selectedDiseases != "":
        data = filter_by_disease(data, selectedDiseases)
    
    return jsonify(data)

# Function to sort data
def sort_data(data, sort_key, sort_order):
    # Check if the sort_key is valid
    if sort_key not in data[0]:
        return data  # Return unsorted data if the key is not valid

    if sort_key == "disease":
        if sort_order == "asc":
            data.sort(key=lambda x: x.get(sort_key, "").lower())
        elif sort_order == "desc":
            data.sort(key=lambda x: x.get(sort_key, "").lower(), reverse=True)
    else:
        data.sort(key=lambda x: int(x.get(sort_key, 0)), reverse=sort_order == "desc")
    return data


# Function to sort data
def transform_temporal_data(data, sort_order, TimeOption):
    transformed_data = []

    for entry in data:
        # Handle different date formats based on TimeOption
        if TimeOption == "monthly" or TimeOption == "yearly":
            # Format the date based on TimeOption
            date_obj = datetime.strptime(entry["date"], "%Y-%m-%dT%H:%M:%S.%f")
            if TimeOption == "monthly":
                date_str = date_obj.strftime("%b %Y")  # format like 'Jan 2023'
            else:  # yearly
                date_str = date_obj.strftime("%Y")  # format like '2023'
        elif TimeOption == "five_yearly":
            # For five-yearly, the date is already a year
            year = int(entry["date"])  # Assuming the year is a string like '1990'
            date_str = f"{year}-{year + 4}"  # format like '2020-2024'

        # Create a new dictionary with the date and the other attributes
        new_entry = {"date": date_str}
        for key, value in entry.items():
            if key not in ["date", "total_count", "freq"]:
                new_entry[key] = value

        transformed_data.append(new_entry)

    # Optionally sort the data
    if sort_order == "asc":
        transformed_data.sort(
            key=lambda x: datetime.strptime(
                x["date"].split("-")[0], "%b %Y" if TimeOption == "monthly" else "%Y"
            )
        )
    elif sort_order == "desc":
        transformed_data.sort(
            key=lambda x: datetime.strptime(
                x["date"].split("-")[0], "%b %Y" if TimeOption == "monthly" else "%Y"
            ),
            reverse=True,
        )

    return transformed_data


@app.route("/get-sorted-data", methods=["GET"])
def get_sorted_data():
    try:
        # Extract parameters from the request
        category = request.args.get("category", "total")
        selectedWindow = request.args.get("selectedWindow", "total")
        sort_key = request.args.get("sortKey", "disease")
        sort_order = request.args.get("sortOrder", "asc")
        selectedDiseases = request.args.get("selectedDiseases", None)
        selectedDataSource = request.args.get("dataSource", "arxiv")

         # Construct the path to the correct data file based on category
        if category == "total":
            data_file_path = os.path.join(current_directory, f'../data/{selectedDataSource}/total_counts.json')
        else:
            if selectedDataSource == "pile":
                data_file_path = os.path.join(current_directory, f'../data/{selectedDataSource}/total_{category}_counts.json')
            else:
                data_file_path = os.path.join(current_directory, f'../data/{selectedDataSource}/{selectedWindow}_{category}_counts.json')
        # Load the data from the correct file
        with open(data_file_path, "r") as file:
            category_data = json.load(file)

        logging.info(f"Data loaded successfully from {data_file_path}")

        # Sort data
        sorted_data = sort_data(category_data, sort_key, sort_order)

        # Filter data by selected disease
        if selectedDiseases:
            sorted_data = filter_by_disease(sorted_data, selectedDiseases)
            logging.debug(f"Filtered Data: {sorted_data}")

        # Pagination parameters
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))

        # Paginate data
        start = (page - 1) * per_page
        end = start + per_page
        paginated_data = sorted_data[start:end]
        length = len(sorted_data)

        return jsonify(length, paginated_data)
    except Exception as e:
        logging.error("An error occurred in get_sorted_data:", exc_info=True)
        return jsonify({"error": str(e)}), 500


def filter_by_disease(sorted_data, selectedDiseases):
    try:
        # Remove spaces and convert to lowercase for each disease in the selectedDiseases list
        selectedDiseasesSet = set(
            disease.replace(" ", "").lower() for disease in selectedDiseases.split(",")
        )

        # Define a lambda function for filtering
        filter_func = (
            lambda item: item.get("disease", "").replace(" ", "").lower()
            in selectedDiseasesSet
        )

        # Use the filter function with the lambda to filter the data
        filtered_data = list(filter(filter_func, sorted_data))
        return filtered_data
    except Exception as e:
        logging.error("An error occurred in filter_by_disease:", exc_info=True)
        # Decide whether to return the unfiltered data or an empty list in case of an error
        return []  # or return sorted_data if that's preferable


def filter_temporal_data(temporal_data, selectedDiseases):
    # Remove spaces and convert to lowercase for each disease in the selectedDiseases list
    selectedDiseasesSet = set(
        disease.replace(" ", "").lower() for disease in selectedDiseases.split(",")
    )

    # Define a lambda function for filtering
    filter_func = lambda entry: any(
        key.replace(" ", "").lower() in selectedDiseasesSet
        for key in entry
        if key != "date"
    )

    # Use the filter function with the lambda to filter the data
    filtered_data = list(filter(filter_func, temporal_data))

    # Creating a new list with filtered entries and retaining only the selected diseases
    final_filtered_data = []
    for entry in filtered_data:
        filtered_entry = {"date": entry["date"]}
        for disease in entry:
            if disease.replace(" ", "").lower() in selectedDiseasesSet:
                filtered_entry[disease] = entry[disease]
        final_filtered_data.append(filtered_entry)

    return final_filtered_data


def extract_disease_names(data_file_path):
    # Load the data from the file
    with open(data_file_path, "r") as file:
        data = json.load(file)

    # Extract and return unique disease names
    return list(set(item["disease"] for item in data))


@app.route("/get-disease-names", methods=["GET"])
def get_disease_names():
    try:
        selectedDataSource = request.args.get("dataSource", "arxiv")
        data_file_path = os.path.join(current_directory, f'../data/{selectedDataSource}/total_counts.json')
        
        disease_names = extract_disease_names(data_file_path)
        return jsonify(disease_names)
    except Exception as e:
        logging.error("An error occurred in get_disease_names:", exc_info=True)
        return jsonify({"error": str(e)}), 500

@app.route("/get-chart-data", methods=["GET"])
def get_chart_data():
    try:
        category = request.args.get("category", "total")
        selectedWindow = request.args.get("selectedWindow", "total")
        sort_key = request.args.get("sortKey", "disease")
        sort_order = request.args.get("sortOrder", "asc")
        selectedDiseases = request.args.get("selectedDiseases", None)
        selectedDataSource = request.args.get("dataSource", "arxiv")

        # Construct the path to the correct data file based on category
        if category == "total":
            data_file_path = os.path.join(
                current_directory, f"../data/{selectedDataSource}/total_counts.json"
            )
        else:
            if selectedDataSource == 'pile':
                data_file_path = os.path.join(
                    current_directory, f"../data/{selectedDataSource}/total_{category}_counts.json"
                )
            else:
                data_file_path = os.path.join(
                    current_directory, f"../data/{selectedDataSource}/{selectedWindow}_{category}_counts.json"
                )

        # Load the data from the correct file
        with open(data_file_path, "r") as file:
            category_data = json.load(file)

        # Sort data
        sorted_data = sort_data(category_data, sort_key, sort_order)

        # Transform data if necessary
        if category == "total_counts":
            sorted_data = transform_total_counts_for_chart(sorted_data)

        # Filter data by selected disease
        if selectedDiseases:
            sorted_data = filter_by_disease(sorted_data, selectedDiseases)

        return jsonify(sorted_data)
    except Exception as e:
        logging.error("An error occurred in get_chart_data:", exc_info=True)
        return jsonify({"error": str(e)}), 500


def transform_total_counts_for_chart(data):
    chart_data = []
    for item in data:
        # Ensure 'disease' and '0' keys exist
        if "disease" in item and "0" in item:
            transformed_item = {"Disease": item["disease"], "Count": item["0"]}
            chart_data.append(transformed_item)
    return chart_data

@app.route("/get-additional-chart-data", methods=["GET"])
def get_additional_chart_data():
    try:
        category = request.args.get("category", "total")
        selectedWindow = request.args.get("selectedWindow", "total")
        sort_key = request.args.get("sortKey", "disease")
        sort_order = request.args.get("sortOrder", "asc")
        selectedDiseases = request.args.get("selectedDiseases", None)
        selectedDataSource = request.args.get("dataSource", "arxiv")
    
        # Construct the path to the correct data file based on category
        if category == "total":
            additonal_data_path = os.path.join(
                current_directory, f"../data/{selectedDataSource}/percentage_difference_gender.json"
            )
        else:
            additonal_data_path = os.path.join(
                current_directory, f"../data/{selectedDataSource}/percentage_difference_{category}.json"
            )

        with open(additonal_data_path, "r") as file:
            additional_data = json.load(file)

        # Sort data
        additional_data = sort_data(additional_data, sort_key, sort_order)

        # Filter data by selected disease
        if selectedDiseases:
            additional_data = filter_by_disease(additional_data, selectedDiseases)

        return jsonify(additional_data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/get-temporal-chart-data", methods=["GET"])
def get_temporal_chart_data():
    try:
        category = request.args.get("category", "total")
        sort_key = request.args.get("sortKey", "disease")
        sort_order = request.args.get("sortOrder", "asc")
        TimeOption = request.args.get("timeOption", "total")
        selectedDiseases = request.args.get(
            "selectedDiseases", "syphilis,lupus,pneumonia"
        )
        startYear = request.args.get("startYear", type=int)
        endYear = request.args.get("endYear", type=int)
        selectedDataSource = request.args.get("dataSource", "arxiv")

        # Construct the path to the correct data file based on category
        temporal_data_path = os.path.join(
            current_directory, f"../data/{selectedDataSource}/{TimeOption}_counts.json"
        )
        with open(temporal_data_path, "r") as file:
            temporal_data = json.load(file)

        # Filter data by years
        if startYear and endYear:
            if TimeOption == "five_yearly":
                # Filter for five-yearly intervals
                temporal_data = [
                    entry
                    for entry in temporal_data
                    if startYear <= int(entry["date"]) <= endYear
                    or startYear <= int(entry["date"]) + 4 <= endYear
                ]
            else:
                # Filter for monthly and yearly data
                temporal_data = [
                    entry
                    for entry in temporal_data
                    if startYear
                    <= datetime.strptime(entry["date"], "%Y-%m-%dT%H:%M:%S.%f").year
                    <= endYear
                ]

        # Sort data
        temporal_data = transform_temporal_data(temporal_data, sort_order, TimeOption)

        # Filter data by selected disease
        if selectedDiseases:
            temporal_data = filter_temporal_data(temporal_data, selectedDiseases)

        return temporal_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
