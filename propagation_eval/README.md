# Propagation Results Analysis

This repository contains a series of Jupyter notebooks dedicated to analyzing specific components of our research findings on logits and co-occurrences in LLMs. 

## Section 1. Co-occurrence Analysis

This section focuses on analyzing co-occurrence counts in the 'The Pile' dataset, examining the relationship between diseases and demographic attributes.

### 1a. Co-occurrence Count Analysis (`co_occurrence_count_analysis.ipynb`)
Analyzes co-occurrence counts with gender and race columns against disease rows. This notebook should cover:
- General disease counts, co-occurrences gender/race, real world prevalence
  - Rows - disease, columns- gender+race, values = co-occurrence counts
  - Subset top 25--> Rows - disease, columns- gender+race
- Variation across windows
  - Figure for showing no variation across window sizes for a given disease demographic pair - hence use one from now on
- Within disease ranks of counts 
  - Table- Rows = disease, columns= gender+race, value = rank within demographic group

### 1b. Real World Counts Comparison (`real_world_counts_comparison.ipynb`)
Compares the real-world prevalence data against the co-occurrence counts obtained from the dataset. 
- Data alignment and preprocessing.
- Comparative analysis and visualization.
  - Rows - disease, columns- gender+race
- Margin of error vs real world prevalence.


## Section 2. Logits in Controlled Setting

This section looks at results from using models trained on 'The Pile' dataset, focusing on Pythia, mamba and T5 models.

### 2a. Top vs. Bottom Rank Comparison (`top_bottom_rank_comparison.ipynb`)
Compares the number of times each model ranks a disease as top vs. bottom for different demographics. 
- Calculate and compare top vs. bottom ranks.
  - Table Rows=templates, columns= gender+race, value=sum of disease top/bottom rank, one table for each model
- Variation across models
  - Table rows= models, race + gender=column, value number of times top across all the diseases and another for bottom

### 2b. Template Robustness Evaluation (`template_robustness_evaluation.ipynb`)
Evaluates variation in logit ranks across each of the templates used in the study.
- Average difference in raw logits within model+disease
- Average difference in logit ranks within model+disease
- Group 1 vs 2 (if keep)
- Tables for above
  - rows-templates, columns- gender+race, value sum of disease top/bottom rank, one table for each model
- Boxplot/violin plot visualise

### 2c. Kendall Tau Scores Analysis (`kendall_tau_scores_analysis.ipynb`)
Calculates and compares Kendall tau scores for co-occurrences and logits, as well as logits vs. real-world prevalence. Should include:
- Comparing co-occurrences with logits- Kendall tau scores race and gender for each model
- Comparing logits and real prevalence- Kendall tau scores race and gender for each model.
- Variation in correlation across overall count size
  - y axis avg Kendall tau, x-axis model size (1 pythia/1 mamba), color quartile of total Co-occurrences for a disease
- Common but non-correlated diseases
  - Rows- disease, columns= count+tau+real world prevalence
  - list where high count but low tau


## Section 3. Model in the Wild Analysis

This section focuses on analyzing models in the wild, including the evaluation of model performance across different languages and alignment strategies.

### 3a. Wild Model Comparative Analysis (`wild_model_comparative_analysis.ipynb`)
Analyzes models "in the wild," focusing on the variability across languages, alignment types, and model sizes. This notebook will cover:
- Count table as above
  - 2x Table models row, race + gender column, value number of times top across all the diseases and another for bottom
- Kendall tau scores 
  - logits vs real world prevalence

### 3b. Language Eval (`lang_eval.ipynb`)
Evaluates the impact of language and model size on model performance. 
- Start with nested table- may need to make one table per language
  - Rows- disease, columns level 1 race/gender, level 2 language, value sum of disease top/bottom rank
- kendall tau scores
  - logits from each language vs real world prevalence

### 3c. Alignment Eval (`align_eval.ipynb`)
Evaluates the impact of language, alignment, and model size on model performance. 
- RLHF vs base
  - Qwen1.5: RLHF vs base
- DPO vs Base
  - Zephyr vs mistral: DPO
  - TULU DPO vs llama: DPO
- IT vs Base
  - TULU SFT vs llama: instruction tuning
  - Mistral-instruct vs mistral: instruction tuning
- Biomedical continue pretraining vs base
  - Bio-mistral 7b vs mistral 7b
  - Llama2 vs Meditron
