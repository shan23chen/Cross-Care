import requests
from dicts.dict_medical import medical_keywords_dict #disease dict
from dicts.dict_drug import drug_keywords_dict #drug_dict
import json
import itertools
import re

# Infini-gram API endpoint
api_url = "https://api.infini-gram.io/"
headers = {"Content-Type": "application/json"}

# Define the list of corpora
corpora = ["v4_piletrain_llama"]  # Can merge multiple corpora

# Function to generate case variations
def generate_case_variations(term):
    words = term.split()
    # Generate all combinations of capitalized and original words
    variations_set = set()
    for combination in itertools.product(*[(word, word.capitalize()) for word in words]):
        # Add the variation with the first word always capitalized and one with all words capitalized
        variations_set.add(' '.join(combination))
    variations_set.add(term.lower())
    variations_set.add(term.upper())
    return variations_set

def extract_total_count_from_message(message):
    # Use regular expression to find the first number in the message
    match = re.search(r"(\d+) occurrences found", message)
    if match:
        # Extract and convert the number to an integer
        return int(match.group(1))
    else:
        # Return None if the pattern is not found
        return 0

# Update the search_documents_count function to use extract_total_count_from_message
def search_documents_count(term, corpora, maxnum=10):
    document_counts = {}
    for corpus in corpora:
        payload = {
            "corpus": corpus,
            "query_type": "search_docs",
            "query": term,
            "maxnum": maxnum  # Request the maximum number of documents to analyze
        }
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            documents = result.get("documents", [])
            message = result.get("message", "")
            # Use the newly implemented function to extract the total count from the message
            total_docs_mentioned = extract_total_count_from_message(message)
            document_counts[corpus] = {
                "total_mentioned": total_docs_mentioned,
                "message": message
            }
        else:
            print(f"Error searching documents for {term} in {corpus}: HTTP {response.status_code}")
    return document_counts

#Iterate over your dictionary of medical terms
# Time complexity O(n^6)
results = []
for disease, disease_terms in medical_keywords_dict.items():
    for drug, drug_terms in drug_keywords_dict.items():
        cooccurrence = (drug, disease)
        cooccurrence_final_count = 0
        for disease_term in disease_terms:
            for drug_term in drug_terms:
                disease_term_variations = generate_case_variations(disease_term)
                for drug_term in drug_terms:
                    drug_term_variations = generate_case_variations(drug_term)
                    for disease_variation in disease_term_variations:
                        for drug_variation in drug_term_variations:
                            term = "{disease_variation} AND {drug_variation}"
                            document_counts = search_documents_count(term, corpora)
                            for corpus in corpora:
                                print(disease_variation, "AND", drug_variation)
                                print(document_counts)  
                                cooccurrence_final_count = document_counts[corpus]["total_mentioned"]

        # Append the disease and its total count to the results list
        results.append({"co-occurence": cooccurrence, "count": cooccurrence_final_count})
        print(f"co-occurence: {cooccurrence}, count: {cooccurrence_final_count}")


# Define the filename you want to save the results to
json_filename = "./results.json"  # Specifying a path in the writable /mnt/data directory

# Use 'with' statement to open the file for writing
with open(json_filename, 'w') as file:
    # Use json.dump() to write the results list directly into the file
    json.dump(results, file, indent=4)  # 'indent=4' for pretty-printing

print(f"Results successfully saved to {json_filename}")
