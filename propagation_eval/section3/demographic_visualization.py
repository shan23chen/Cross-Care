import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model_grouping import model_group
from collections import Counter

# Define your categories and any other global configurations
race_categories = ["asian", "black", "white", "hispanic", "indigenous", "pacific islander"]
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
    softmax_list = []
    for i in results_rank_comb.iterrows():
        demographic_rank = i[1]['demographic_rank']
        logits_rank = i[1]['logits_ranking']
        sorted_pairs = sorted(list(zip(demographic_rank, logits_rank)))
        sorted_logits = [i[1] for i in sorted_pairs]
        softmax_logits = list(softmax(sorted_logits))
        softmax_list.append(str(softmax_logits))
    results_rank_comb['sorted_softmax_logits'] = softmax_list
    rank_df_valid = results_rank_comb[(results_rank_comb['model_name'] != 'EleutherAI/pile-t5-large') & (results_rank_comb['model_name'] != 'EleutherAI/pile-t5-base')]

    return rank_df_valid

def generate_demo_ratio_df(rank_df_valid_4lang, demographic='race'):
    lang_demo_ratio_dict = {}
    for language in ['en', 'zh', 'es', 'fr']:
        demo_ratio_plot_df = pd.DataFrame()
        rank_df_valid = rank_df_valid_4lang[rank_df_valid_4lang['language'] == language]
        for model_name, model_group in rank_df_valid.groupby(['model_name']):
            # print(model_group)
            softmax_logits_total = np.array([eval(i[1]['sorted_softmax_logits']) for i in model_group.iterrows()])
            softmax_logits_disease_mean = np.sum(softmax_logits_total, axis=0)/softmax_logits_total.shape[0]
            # print(softmax_logits_disease_mean)
            demo_ratio_plot_df[model_name[0]] = softmax_logits_disease_mean
        if demographic == 'race':
            demo_ratio_plot_df['demographic'] = sorted(race_categories)
        else:
            demo_ratio_plot_df['demographic'] = sorted(gender_categories)
        demo_ratio_plot_df.set_index('demographic', inplace=True)
        lang_demo_ratio_dict[language] = demo_ratio_plot_df
    return lang_demo_ratio_dict

def generate_top_bot_df(dataframe, grouping, demographic_position='top'):
    models_to_include = model_group[grouping]
    filtered_df_4lang = dataframe[dataframe['model_name'].isin(models_to_include)].copy()
    if demographic_position == 'top':
        target_position = 0
    elif demographic_position == 'bottom':
        target_position = -1
    elif demographic_position == 'second_bottom':
        target_position = -2
    else:
        raise ValueError("demographic_position must be 'top', 'bottom', or 'second_bottom'")
    filtered_df_4lang['target_demographic'] = filtered_df_4lang['demographic_rank'].apply(
        lambda x: x[target_position] if isinstance(x, list) and len(x) > abs(target_position) else None
    )
    
    lang_top_bot_dict = {}
    for lang in ['en', 'zh', 'es', 'fr']:
        filtered_df = filtered_df_4lang[filtered_df_4lang['language'] == lang]
        top_bot_dict = {}
        for model in models_to_include:
            # max_list = []
            # min_list = []
            temp_dict = dict(Counter(filtered_df[filtered_df['model_name'] == model]['target_demographic']))
            temp_dict = dict(sorted(temp_dict.items()))
            top_bot_dict[model] = temp_dict
        top_bot_df = pd.DataFrame(top_bot_dict)
        lang_top_bot_dict[lang] = top_bot_df
    return lang_top_bot_dict

def full_language_visualization(grouping, model_dist_dict, demographic='race', hf_mode='hf', plot_mode='ratio', rotation=0):
    models = model_group[grouping] 
    fig, ax = plt.subplots(constrained_layout=True)
    fig.set_figheight(5)
    fig.set_figwidth(15)
    x_pos = np.array(list(range(0, 2*len(model_dist_dict['en'][models].columns), 2))).astype(np.float32)
    # print(x_pos)  

    labels = list(model_dist_dict['en'].index)
    colors = ['firebrick', 'blue', 'green', 'orange', 'purple', 'gray'][:len(labels)]
    # print(labels)

    for language in ['en', 'zh', 'es', 'fr']:
        rows = 0
        model_dist_df = model_dist_dict[language][models]
        for i in model_dist_df.iterrows():
            # print(i[1].values)
            ax.bar(x_pos, i[1].values, bottom=model_dist_df.iloc[:rows].sum(axis=0), color=colors[rows], width=0.3)
            rows += 1
        x_pos += 0.4
    
    lang_labels_pos = []
    start = 0
    for i in range(len(x_pos)):
        temp = []
        lang_start = start
        for _ in range(4):
            temp.append(lang_start)
            lang_start += 0.4
        lang_labels_pos += temp
        start += 2
    # print(lang_labels_pos)
    
    model_labels = []
    for name in models:
        try:
            model_labels.append(name.split('/')[1])
        except:
            model_labels.append(name)
            
    ax.set_xlabel('model name')
    ax.xaxis.set_label_coords(0.5,-0.15)
    ax.set_ylabel('demographic count across disesases')
    sec_x = ax.secondary_xaxis('top')
    sec_x.set_xticks(lang_labels_pos, ['en', 'zh', 'es', 'fr']*len(models))
    ax.set_xticks(np.array(range(0, 2*len(model_dist_dict[language][models].columns), 2))+0.6, model_labels, rotation=rotation)
    # ax.set_xticks(lang_labels_pos, ['en', 'zh', 'es', 'fr']*len(models), minor=True)
    ax.set_title(f'{demographic} distribution for each {grouping} model across diseases ({hf_mode} America)')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), labels=labels, labelcolor=colors, ncols=6)
    plt.show()
    fig.savefig(f'{grouping}_{demographic}_{hf_mode}_{plot_mode}_distribution.png')
    
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
