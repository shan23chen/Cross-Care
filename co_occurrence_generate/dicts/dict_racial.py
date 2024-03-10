racial_keywords_dict = {
    "White/Caucasian": [
        "White", "Caucasian", "Anglo", "European", "European-American", "European-Americans",
        "Western-European", "Eastern-European", "Northern-European", "Southern-European",
        "Western-Europeans", "Eastern-Europeans", "Northern-Europeans", "Southern-Europeans",
        "Whites", "Caucasians", "Anglos", "Europeans"
    ],
    "Black/African American": [
        "Black", "Afro-American", "African", "Afro-Caribbean", 
        "African-American", "Afro American", "Blacks", 
        "Afro-Americans", "Africans", "Afro-Caribbeans", "African-Americans", "Afro Americans",
        "AA", "Af Amr"
    ],
    "Hispanic/Latino": [
        "Hispanic", "Latino", "Latina", "Latino/a", "Latinx", "Chicano", "Chicana", 
        "Chicano/a", "Chicanx", "Latin", "Latine", "Latin-American",
        "Hispanics", "Latinos", "Latinas", "Chicanos", 
        "Chicanas", "Latins", "Latines", "Latin-Americans"
    ],
    "Asian": [
        "Asian", 
        "East-Asian", "South-Asian", "Southeast-Asian", "Asian-American",
        "Asians", "East-Asians", "South-Asians", "Southeast-Asians", "Asian-Americans"
    ],
    "Native American/Indigenous": [
        "Native American", "American Indian", "Alaskan Native", "Indigenous", 
        "Inuit", "Aleut", "Alaska Native", "Native-American", "American-Indian", "Alaskan-Native", "Alaska-Native", "Native Americans", 
        "American Indians", "Alaskan Natives", "Inuits", "Aleuts", 
        "Alaska Natives", "Native-Americans", "American-Indians", 
        "Alaskan-Natives", "Alaska-Natives"
    ],
    "Pacific Islander": [
        "Pacific Islander", "Hawaiian", "Pacific-Islander", "Native Hawaiian",
        "Pacific Islanders", "Hawaiians", "Pacific-Islanders"
    ]
}

racial_keywords_dict = {key.lower(): [word.lower() for word in value] 
                        for key, value in racial_keywords_dict.items()}
