# TODO 

---

### Checkpoint 1- Arxiv POC (Proof of Concept)
- **Finalize Keywords Collection**
  - Cancer Types:
    - Awaiting response from an oncology ontologist for appropriate vocabulary.
  - ~~Normalization Terms / Other Diseases (in progress)~~
  - Cancer Drugs (in progress)
- ~~Race + Gender:~~
  - ~~Cross-check race with SDOH paper: https://ascopubs.org/doi/abs/10.1200/CCI.22.00196.~~
  - Additional:
    - ~~Consider adding Abby’s list of honorifics for expanded gender terms.~~
    - ~~Nationality terms from Abby's list (used for the SDOH paper).~~

- **Test Running Co-occurrence Analysis**
  - Using only Arxiv (local database).

### Checkpoint 2- Full Dataset Co-occurrences
- **Expand Run to Complete Datasets**
  - Redpajama
  - Pile
  - Mimic Notes

- **Considerations**
  - Should an internal dataset also be included?

- **Setup Virtual Machine**
  - Storage Requirement: 5TB
  - Need to find AWS credit for this setup.

---

## Repository Structure (Desired):

```
LLM_Bias/
│
├── data/
│   ├── counts/  
│   ├── raw_data/  (Too big to fit here naturally)
│   └── filtered/   (Also too big to fit here)
│
├── src/
│   ├── __init__.py
│   ├── jsonl_data_filtering.py
│   └── data_analysis.py
│
├── dicts/
│   ├── dict_medical.py
│   ├── dict_gender.py
│   └── dict_racial.py
│
├── keywords/
│   ├── keywords_medical.py
│   ├── keywords_gender.py
│   └── keywords_racial.py
│
├── tests/
│   └── test_data_filtering.py
│
├── docs/
│   └── README.md
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── results/
│   └── figures/
│
├── configs/
│   ├── stackexchange.yaml
│   ├── arxiv.yaml
│   ├── wikipedia.yaml
│   ├── c4.yaml
│   ├── books.yaml
│   ├── github.yaml
│   └── commoncrawl.yaml
│
└── main.py
```

## Extracting Relevant Text from Training Data:

### Step 1:
Define keyword dictionaries that relate to each disease, race, and gender.

### Step 2:
Filter all documents from pre-training data that mention disease AND (gender OR race).

### Step 3:
Deal with ambiguous keywords, e.g., ensuring all mentions of ‘white’ and ‘black’ relate to ethnicity and not actual colors (”the black car was for sale”), and that ‘aids’ relate to the disease and not the unrelated noun (hearing or walking aids) and the verb (she ‘aids’ him). This is done using a biomedical NER tagger that is configured to only extract keyword matches that are classified as pertaining to the disease or the race (personal background). In this step, all irrelevant occurrences of the keywords are flagged, so they don’t count in the subsequent co-occurrence analysis.

## Datasets

Note the datasets analyzed are all English datasets. 

- Arxiv (88 GB)
    - Total data loaded and filtered (Keyword Present - Medical AND Racial OR Gender): 77788
    - Filtered Size (Keyword Present - Medical AND Racial OR Gender): 4.6 GB
    - Filtered Size (Ambgious Keywords Filtering):
    - Meta Data Keys: timestamp, yymm, arxiv_id, language, url
- GitHub (213 GB)
    - Filtered Size (Keyword Present - Medical AND Racial OR Gender): 2.8 GB
    - Filtered Size (Ambgious Keywords Filtering): 
- Stackexchange (74.5 GB)
    - Total data loaded and filtered: 9212
    - Filtered Size (Keyword Present - Medical AND Racial OR Gender): 70.1 MB
    - Filtered Size (Ambgious Keywords Filtering):
    - Meta Data Keys: language, url, timestamp, question_score
- Wikipedia (112 GB) -> When filtered for English only (20.3GB)
    - Filtered Size (Keyword Present - Medical AND Racial OR Gender): 1.6 GB
    - Filtered Size (Ambgious Keywords Filtering):
    - Meta Data Keys: title, url, language, timestamp
- Commoncrawl
    - 2019-30 Folder: (238 GB)
    - 2020-05 Folder: (285 GB)
    - 2021-04 Folder: (274 GB)
    - 2022-05 Folder: (251 GB)
    - 2023-06 Folder: (289 GB)
    - Filtered Size (Keyword Present - Medical AND Racial OR Gender): XX GB
- C4 (807 GB)
    - Filtered Size (Keyword Present - Medical AND Racial OR Gender): 19.4 GB
    - Total data loaded and filtered: 2340188
- Books (100.4 GB)
    - Filtered Size (Keyword Present - Medical AND Racial OR Gender): 52.3 GB
    - Filtered Size (Keyword Present - Medical AND Racial OR Gender): 40.5 GB (When removing latex formatting)
    - Total data loaded and filtered: 76297

## Downloading the Training Data:

To download only the files pertaining to RedPyjama from the dataset, follow the steps below. Detailed documentation for the download can be found [here](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T).

```bash
# Download the urls.txt file which contains URLs to all the datasets
wget 'https://data.together.xyz/redpajama-data-1T/v1.0.0/urls.txt'

# Get the urls related to each of the datasets in RedPajama
grep “arxiv” urls.txt > arxiv_urls.txt
# ... [repeat for other datasets]

# Use the modified script to download only the specific files
while read line; do
    dload_loc=${line#https://data.together.xyz/redpajama-data-1T/v1.0.0/}
    mkdir -p $(dirname $dload_loc)
    wget "$line" -O "$dload_loc"
done < arxiv_urls.txt
# ... [repeat for other datasets]


# for Wikipedia, select only english articles:
jq -c 'select(.meta.language == "en")' wiki.jsonl > wiki_en.jsonl

# if you dont have jq:

## on Ubuntu:
sudo apt-get install jq

## on macOS with Homebrew:
brew install jq
```

## How to Use

### Configuration Files
Configuration files are used to specify the parameters for data filtering and analysis. These are stored in the configs/ directory and are written in YAML format. Each dataset should have its own configuration file.

Example of a configuration file (wikipedia.yaml):

```
data:
  input_file_path: 'data/raw_data/wikipedia.jsonl'
  output_folder_path: 'data/filtered/Wikipedia'
  metadata_keys: 
    - "language"
    - "url"
    - "timestamp"
processing:
  remove_latex: true
  save_file: true
  filename: 'wikipedia_filtered.csv'
  total_texts_filename: 'tot_texts_wiki.txt'

```


### Data Filtering and Analysis Scripts

Two main scripts are provided for data processing:

- main_folders.py: For datasets organized in folders with multiple .jsonl files.
- main_single_file.py: For datasets contained in a single .jsonl file.

### Running the Scripts
To run the scripts, use the following command in your terminal, replacing [script_name] with the name of the script you want to run (main_folders or main_single_file) and [config_name] with the name of your configuration file (without the .yaml extension):

```
python [script_name].py [config_name]

```

example:

```
python main_single_file.py wikipedia

```

### This will:

Filter the data based on the terms defined in the dictionaries located in the dicts/ folder.
Perform a co-occurrence analysis.
Save the filtered data and analysis results in specified output directories.

## Contributing
Contributions to improve the code or add additional functionalities are welcome! Please ensure to follow the existing code structure and comment appropriately.
