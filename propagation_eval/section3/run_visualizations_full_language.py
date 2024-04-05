import argparse
from demographic_visualization import load_and_prepare_data, visualize_demographic_rankings_filtered, generate_demo_ratio_df, generate_top_bot_df, full_language_visualization

def main(demographic, language):
    # Load and prepare the data
    df = load_and_prepare_data(demographic=demographic, language=language)

    # List of demographic positions to visualize
    demographic_positions = ['top', 'bottom', 'second_bottom']

    # List of model groups to include in the visualization
    model_groups = ['pythia', 'mamba', 'qwen', 'llama', 'mistral', 'api_model', 'biomed', 'scaling_law', 'rlhf_llama']

    for grouping in model_groups:
        for position in demographic_positions:
            ratio_df_dict = generate_demo_ratio_df(df, demographic)
            top_bot_dict = generate_top_bot_df(df, position)
            full_language_visualization(grouping, ratio_df_dict, demographic=demographic, plot_mode='ratio')
            full_language_visualization(grouping, top_bot_dict, demographic=demographic, plot_mode='top_bot')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize demographic rankings for specified models and positions.")
    parser.add_argument("--demographic", type=str, default="race", choices=["race", "gender"],
                        help="The demographic category to analyze (default: race).")
    parser.add_argument("--language", type=str, default="en",
                        help="The language of the models to analyze (default: en).")
    
    args = parser.parse_args()

    main(args.demographic, args.language)
