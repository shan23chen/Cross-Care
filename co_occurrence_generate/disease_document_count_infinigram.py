import requests
import json
import itertools
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
# Import your dictionaries here
from dicts.dict_medical import medical_keywords_dict  # Assuming these are your custom modules


api_url = "https://api.infini-gram.io/"
headers = {"Content-Type": "application/json"}
corpora = ["v4_piletrain_llama"]


def extract_total_count_from_message(message):
    match = re.search(r"(\d+) occurrences found", message)
    if match:
        return int(match.group(1))
    else:
        return 0

def search_documents_for_corpus(term, corpus, maxnum=10):
    payload = {
        "corpus": corpus,
        "query_type": "search_docs",
        "query": term,
        "maxnum": maxnum
    }
    return requests.post(api_url, json=payload, headers=headers)

def search_documents_count(term, corpora, maxnum=10):
    document_counts = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_corpus = {executor.submit(search_documents_for_corpus, term, corpus, maxnum): corpus for corpus in corpora}
        for future in as_completed(future_to_corpus):
            corpus = future_to_corpus[future]
            try:
                response = future.result()
            except Exception as exc:
                print(f"{corpus} generated an exception: {exc}")
            else:
                if response.status_code == 200:
                    result = response.json()
                    message = result.get("message", "")
                    total_docs_mentioned = extract_total_count_from_message(message)
                    document_counts[corpus] = {
                        "total_mentioned": total_docs_mentioned,
                        "message": message
                    }
                else:
                    print(f"Error searching documents for {term} in {corpus}: HTTP {response.status_code}")
    return document_counts

results = []
for disease, disease_terms in medical_keywords_dict.items():
    disease_final_count = 0
    for disease_term in disease_terms:
        term = f"{disease_term}"
        document_counts = search_documents_count(term, corpora)
        for corpus, count_info in document_counts.items():
            print(disease_term)
            print(count_info)
            disease_final_count += count_info["total_mentioned"]

    results.append({"disease": disease, "count": disease_final_count})
    print(f"co-occurrence: {disease}, count: {disease_final_count}")

json_filename = "./results_disease_document_counts.json"
with open(json_filename, 'w') as file:
    json.dump(results, file, indent=4)

print(f"Results successfully saved to {json_filename}")
