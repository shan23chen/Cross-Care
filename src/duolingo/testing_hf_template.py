from templates import DiseaseDemographicTemplates

if __name__ == '__main__':
    disease_demographic_templates = DiseaseDemographicTemplates()
    
    # Example parameters
    language = 'zh'
    demographic_choice = 'gender'
    
    diseases = disease_demographic_templates.get_diseases(language)
    templates = disease_demographic_templates.get_templates(language)
    demographic_columns = disease_demographic_templates.get_demographics(language, demographic_choice)
    demo_query = disease_demographic_templates.get_demographic_query(language, demographic_choice)

    print(diseases)
    print(templates)
    print(demographic_columns)
    print(demo_query)