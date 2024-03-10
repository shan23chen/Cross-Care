import requests
from dicts.dict_medical import medical_keywords_dict
import json
import itertools

# Infini-gram API endpoint
api_url = "https://api.infini-gram.io/"
headers = {"Content-Type": "application/json"}

# Define the list of corpora
corpora = ["v4_piletrain_llama", "v4-piletest"] # Can merge multiple corpora 

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

# Function to make the API request
def count_term(term, corpora):
    total_count = 0
    for corpus in corpora:
        payload = {
            "corpus": corpus,
            "query_type": "count",
            "query": term
        }
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            total_count += result.get("count", 0)
        else:
            print(f"Error for {term} in {corpus}: HTTP {response.status_code}")
    return total_count

# Iterate over your dictionary of medical terms
results = []
for disease, terms in medical_keywords_dict.items():
    disease_final_count = 0
    for term in terms:
        term_variations = generate_case_variations(term)
        for variation in term_variations:
            count = count_term(variation, corpora)
            print(f"Term: {variation}, Count: {count}")
            disease_final_count += count
    # Append the disease and its total count to the results list
    results.append({"disease": disease, "0": disease_final_count})

# Write the results to a JSON file
with open("total_counts.json", "w") as outfile:
    json.dump(results, outfile)
