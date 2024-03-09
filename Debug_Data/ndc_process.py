import json
import requests
import zipfile
import io
import pandas as pd


#### DRUG FILTER ####
def create_filter_list():
    # Brand names
    brand_names_wiki = [
        "Abilify",
        "Humira",
        "Nexium",
        "Crestor",
        "Enbrel",
        "Advair Diskus, Seretide",
        "Remicade",
        "Lantus Solostar",
        "Neulasta",
        "Copaxone",
        "Rituxan, MabThera",
        "Spiriva",
        "Januvia",
        "Lantus",
        "Atripla",
        "Cymbalta",
        "Avastin",
        "Lyrica",
        "OxyContin",
        "Celebrex",
        "Epogen",
        "Truvada",
        "Diovan",
        "Levemir",
        "Gleevec, Glivec",
        "Herceptin",
        "Vyvanse",
        "Lucentis",
        "Zetia",
        "Combivent",
        "Symbicort",
        "Namenda",
        "NovoLog FlexPen",
        "Xarelto",
        "NovoLog",
        "Humalog",
        "Suboxone",
        "Viagra",
        "Seroquel XR",
        "Incivo",
        "AndroGel",
        "Enoxaparin",
        "Ritalin",
        "ProAir HFA",
        "Alimta",
        "Victoza",
        "Synagis",
        "Avonex",
        "Renvela",
        "Rebif",
        "Cialis",
        "Gilenya",
        "Nasonex",
        "Stelara",
        "Restasis",
        "Budesonide",
        "Acetaminophen/hydrocodone",
        "Flovent HFA",
        "Lovaza",
        "Prezista",
        "Isentress",
        "Janumet",
        "Procrit, Eprex",
        "Doxycycline",
        "Orencia",
        "Amphetamine/dextroamphetamine",
        "Vesicare",
        "Dexilant",
        "Humalog KwikPen",
        "Neupogen",
        "Lidocaine",
        "Lunesta",
        "Fenofibrate",
        "Zytiga",
        "Reyataz",
        "Sensipar",
        "Metoprolol",
        "AcipHex",
        "Synthroid",
        "Avonex Pen",
        "Prevnar 13",
        "Xolair",
        "Lipitor",
        "Levothyroxine",
        "Benicar",
        "Stribild",
        "Zostavax",
        "Pradaxa",
        "Vytorin",
        "Tamiflu",
        "Xgeva",
        "Evista",
        "Xeloda",
        "Aranesp",
        "Ventolin HFA",
        "divalproex sodium",
        "Afinitor",
        "Betaseron, Betaferon",
        "Adderall XR",
        "Complera",
    ]

    # Generic names
    generic_names_wiki = [
        "Aripiprazole",
        "Adalimumab",
        "Esomeprazole",
        "Rosuvastatin",
        "Etanercept",
        "Fluticasone/salmeterol",
        "Infliximab",
        "Insulin glargine",
        "Pegfilgrastim",
        "Glatiramer",
        "Rituximab",
        "Tiotropium bromide",
        "Sitagliptin",
        "Insulin glargine",
        "Emtricitabine/tenofovir/efavirenz",
        "Duloxetine",
        "Bevacizumab",
        "Pregabalin",
        "Oxycodone",
        "Celecoxib",
        "Epoetin alfa",
        "Tenofovir/emtricitabine",
        "Valsartan",
        "Insulin detemir",
        "Imatinib",
        "Trastuzumab",
        "Lisdexamfetamine",
        "Ranibizumab",
        "Ezetimibe",
        "Ipratropium bromide/salbutamol",
        "Budesonide/formoterol",
        "Memantine",
        "Insulin aspart",
        "Rivaroxaban",
        "Insulin aspart",
        "Insulin lispro",
        "Buprenorphine",
        "Sildenafil",
        "Quetiapine",
        "Telaprevir",
        "Testosterone gel",
        "Enoxaparin",
        "Methylphenidate",
        "Salbutamol",
        "Pemetrexed",
        "Liraglutide",
        "Palivizumab",
        "Interferon beta 1a",
        "Sevelamer",
        "Interferon beta 1a",
        "Tadalafil",
        "Fingolimod",
        "Mometasone",
        "Ustekinumab",
        "Ciclosporin ophthalmic emulsion",
        "Budesonide",
        "Acetaminophen/hydrocodone",
        "Fluticasone propionate",
        "Omega-3 fatty acid ethyl esters",
        "Darunavir",
        "Raltegravir",
        "Sitagliptin/metformin",
        "Epoetin alfa",
        "Doxycycline",
        "Abatacept",
        "Amphetamine mixed salts",
        "Solifenacin",
        "Dexlansoprazole",
        "Insulin lispro",
        "Filgrastim",
        "Lidocaine",
        "Eszopiclone",
        "Fenofibrate",
        "Abiraterone",
        "Atazanavir",
        "Cinacalcet",
        "Metoprolol",
        "Rabeprazole",
        "Levothyroxine",
        "Olmesartan",
        "Pneumococcal conjugate vaccine",
        "Omalizumab",
        "Atorvastatin",
        "Levothyroxine",
        "Olmesartan/hydrochlorothiazide",
        "Elvitegravir/cobicistat/emtricitabine/tenofovir",
        "Zostavax",
        "Dabigatran",
        "Ezetimibe/simvastatin",
        "Oseltamivir",
        "Denosumab",
        "Raloxifene",
        "Capecitabine",
        "Darbepoetin alfa",
        "Salbutamol",
        "Valproate",
        "Everolimus",
        "Interferon beta 1b",
        "Amphetamine mixed salts",
        "Emtricitabine/Rilpivirine/Tenofovir disoproxil fumarate",
    ]

    drug_names_twitter = [
        "tylenol pm",
        "antibiotics",
        "muscle relaxers",
        "zofran",
        "benadryl",
        "pitocin",
        "steroids",
        "sudafed",
        "acetaminophen",
        "adderall",
        "painkillers",
        "insulin",
        "castor oil",
        "anti anxiety meds",
        "ibuprofen",
        "vaccines",
        "lupron",
        "heparin",
        "fentanyl",
        "narcotics",
        "bio oil",
        "lifewithazofranpump",
        "triamcinolone",
        "sleeping medicine",
        "steroid nasal spray",
        "vicodeine",
        "hydrocodone bitartrate",
        "celebrex",
        "sleeping pills",
        "insulin drip",
        "paracetamol",
        "nicotine",
        "melatonin",
        "prenatal pills",
        "flu medication",
        "pills",
        "nexplanon",
        "zofranpump",
        "aspirin",
        "warfarin",
        "nausea pills",
        "anaesthetic",
        "hydrocortisone cream",
        "pitosin",
        "baby aspirin",
        "gravol",
        "anesthesia",
        "steroid injections",
        "caffeine pills",
        "antacids",
        "tylenol codeine",
        "pepto bismol",
    ]

    # combine into one list
    drug_list = brand_names_wiki + generic_names_wiki + drug_names_twitter

    return drug_list


#### NDC PROCESS ####
def download_and_extract_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
            for zipinfo in thezip.infolist():
                with thezip.open(zipinfo) as thefile:
                    return json.load(thefile)
    else:
        print("Failed to download file")
        return None


def extract_brand_and_generic_names(data, filter_list):
    brand_and_generic_names = []
    for item in data["results"]:
        brand_name = item.get("brand_name", "Unknown")
        generic_name = item.get("generic_name", "Unknown")
        if brand_name.lower() in filter_list or generic_name.lower() in filter_list:
            brand_and_generic_names.append((brand_name, generic_name))
    return brand_and_generic_names


def read_extracted_data_to_df(file_path):
    return pd.read_csv(
        file_path, sep="\t", header=None, names=["Brand Name", "Generic Name"]
    )


def test_filter_list_presence(file_path, filter_list):
    df = read_extracted_data_to_df(file_path)
    filter_set = set(drug.lower() for drug in filter_list)

    no_match_count = 0
    for index, row in df.iterrows():
        brand = row["Brand Name"].lower() if isinstance(row["Brand Name"], str) else ""
        generic = (
            row["Generic Name"].lower() if isinstance(row["Generic Name"], str) else ""
        )

        if not (brand in filter_set or generic in filter_set):
            no_match_count += 1
            print(
                f"No match found in row {index}: Brand - {brand}, Generic - {generic}"
            )

    if no_match_count == 0:
        print("All rows contain at least one word from the filter list.")
    else:
        print(
            f"There are {no_match_count} rows that do not contain any words from the filter list."
        )


def create_drug_keywords_dict(df_path, filter_list):
    drug_df = read_extracted_data_to_df(df_path)

    drug_keywords_dict = {}
    filter_set = set(drug.lower() for drug in filter_list)

    for index, row in drug_df.iterrows():
        for col in ["Brand Name", "Generic Name"]:
            drug_name = row[col]
            if isinstance(drug_name, str):  # Check if drug name is not NaN
                drug_name_lower = drug_name.lower()
                # Check if this drug name (in any case) is in the filter list
                if drug_name_lower in filter_set:
                    if drug_name_lower not in drug_keywords_dict:
                        drug_keywords_dict[drug_name_lower] = set()
                    drug_keywords_dict[drug_name_lower].add(drug_name)

    # Convert sets to lists for the final output
    for key in drug_keywords_dict:
        drug_keywords_dict[key] = list(drug_keywords_dict[key])

    return drug_keywords_dict


def save_dict_as_py(dictionary, filename):
    with open(filename, "w") as file:
        file.write(f"drug_keywords_dict = {str(dictionary)}\n")


def save_dict_as_keywords_py(dictionary, filename):
    with open(filename, "w") as file:
        file.write("drug_keywords = [word.lower() for word in [\n")
        for key, words in dictionary.items():
            comment = f"    #{key}\n"
            words_str = ", ".join(f"'{word}'" for word in words)
            file.write(comment + f"    {words_str}, \n\n")
        file.write("]]\n")


if __name__ == "__main__":
    raw_filter_list = create_filter_list()
    filter_list = set(drug.lower() for drug in raw_filter_list)

    # URL of the ZIP file
    url = "https://download.open.fda.gov/drug/ndc/drug-ndc-0001-of-0001.json.zip"

    # Download and extract JSON data
    data = download_and_extract_json(url)

    if data:
        # Extract and filter brand and generic names
        extracted_data = extract_brand_and_generic_names(data, filter_list)

        # Save the extracted data to a tsv
        with open("Debug_Data/extracted_data.tsv", "w") as file:
            for brand, generic in extracted_data:
                file.write(f"{brand}\t{generic}\n")

    else:
        print("No data was extracted.")

    # check every row has at least one word from the filter list
    test_filter_list_presence("Debug_Data/extracted_data.tsv", filter_list)

    # now convert the tsv to a dictionary
    drug_dict = create_drug_keywords_dict("Debug_Data/extracted_data.tsv", filter_list)

    # Print a sample from the dictionary
    for key, value in list(drug_dict.items())[:50]:
        print(f"{key}: {value}")

    # check if length of dictionary is more than filter list
    print(f"Length of dictionary: {len(drug_dict)}")
    print(f"Length of filter list: {len(filter_list)}")

    # Save the dictionary as a .py file
    save_dict_as_py(drug_dict, "dicts/dict_drugs.py")

    # Save the dictionary in the desired format
    save_dict_as_keywords_py(drug_dict, "keywords/keywords_drugs.py")
