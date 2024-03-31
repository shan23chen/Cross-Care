import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model_grouping import model_group

# Define your categories and any other global configurations
race_categories = ["asian", "black", "hispanic", "indigenous", "pacific islander"]
gender_categories = ["male", "female", "non-binary"]
demographic = 'race'  # Could be 'race' or 'gender'
logits_dir = "../../logits_results"

def softmax(x):
    """Apply softmax to an array of logits."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def load_and_prepare_data(demographic, language):
    """Load and prepare dataset based on demographic and language."""
    if demographic == 'race':    
        df = pd.read_parquet(os.path.join(logits_dir, 'joined/combined_race_logits.parquet'))
    else:
        df = pd.read_parquet(os.path.join(logits_dir, 'joined/combined_gn_logits.parquet'))
                                      
    df.loc[df['model_name'] == 'cohere', 'logit_type'] = 'hf'
    df.loc[df['logit_type'] == 'azure', 'logit_type'] = 'hf'
    df.loc[df['logit_type'] == 'cohere', 'model_name'] = 'cohere'

    if language is not None:
        df = df[(df['language'] == str(language)) & (df['logit_type'] == 'hf') & (df['window'] == '250') & (df['location_preprompt'] == 1) & (df['template'] < 10)]
    else: 
        df = df[(df['logit_type'] == 'hf') & (df['window'] == '250') & (df['location_preprompt'] == 1) & (df['template'] < 10)]
    
    results = df.groupby(['disease', 'model_name', 'demographic', 'language'])['logit_value'].mean().reset_index()

    # Assuming 'results' DataFrame now includes a 'language' column.
    results_rank = results.groupby(['disease', 'model_name', 'language']).apply(lambda x: x.sort_values(["logit_value"], ascending = False)).reset_index(drop=True)
    results_rank.rename(columns={"logit_value": "mean_logit_value"}, inplace=True)

    models = results_rank['model_name'].unique()
    diseases = results_rank['disease'].unique()
    languages = results_rank['language'].unique()  # Extract unique languages

    results_rank_comb = pd.DataFrame()

    for model in models:
        for disease in diseases:
            for language in languages:  # Iterate through languages
                filter_criteria = (results_rank['model_name'] == model) & \
                                (results_rank['disease'] == disease) & \
                                (results_rank['language'] == language)  # Filter by language
                sort_df = results_rank[filter_criteria].sort_values('mean_logit_value', ascending=False).reset_index(drop=True)
                
                if not sort_df.empty:  # Check if dataframe is not empty
                    numerical_ranking = sort_df['mean_logit_value'].values
                    ranking = sort_df['demographic'].values
                    
                    row = pd.DataFrame({
                        'disease': [disease],
                        'model_name': [model],
                        'language': [language],  # Include language in the row
                        'demographic_rank': [ranking.tolist()],  # Convert to list directly
                        'logits_ranking': [numerical_ranking.tolist()]  # Convert to list directly
                    })
                    results_rank_comb = pd.concat([results_rank_comb, row], ignore_index=True)

    results_rank_comb['prob_distribution'] = results_rank_comb['logits_ranking'].apply(softmax)

    return results_rank_comb

def visualize_demographic_rankings_filtered(dataframe, grouping, demographic_position='top'):
    """
    Visualizes the count of times each demographic is ranked at the specified position (top, bottom, or second_bottom)
    for a specified list of models in the dataset.
    """
    models_to_include = model_group[grouping] 
    filtered_df = dataframe[dataframe['model_name'].isin(models_to_include)].copy()
    
    if demographic_position == 'top':
        target_position = 0
    elif demographic_position == 'bottom':
        target_position = -1
    elif demographic_position == 'second_bottom':
        target_position = -2
    else:
        raise ValueError("demographic_position must be 'top', 'bottom', or 'second_bottom'")
    
    filtered_df['target_demographic'] = filtered_df['demographic_rank'].apply(
        lambda x: x[target_position] if isinstance(x, list) and len(x) > abs(target_position) else None
    )
    
    grouped_data = filtered_df.groupby('model_name')['target_demographic'].value_counts().unstack(fill_value=0)
    
    fig, ax = plt.subplots(figsize=(14, 8))
    grouped_data.plot(kind='bar', stacked=True, ax=ax)
    title_map = {
        'top': f'Top-Ranked Demographic Count for Selected Models: {grouping}',
        'bottom': f'Bottom-Ranked Demographic Count for Selected Models: {grouping}',
        'second_bottom': f'Second-to-Bottom-Ranked Demographic Count for Selected Models: {grouping}'
    }
    ax.set_title(title_map[demographic_position])
    ax.set_ylabel('Count of Occurrences')
    ax.set_xlabel('Model Names')
    # plt.xticks(rotation=45)
    plt.legend(title='Demographics', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("This module provides visualization functions for demographic rankings and should not be run directly.")
