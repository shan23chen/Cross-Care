# Real World Data

## Data Sources
Two primary sources were used to collect the real-world data for the diseases. The first source was the Global Burden of Disease (GBD) study, which provides prevalence values for a wide range of diseases stratified by sex. The second source was the National Health Interview Survey which provides prevalence values for a wide range of diseases stratified by race. 

### Global Burden of Disease (GBD) Data
Keywords for all diseases were attempted to query the database for Sex Prevalence via the 2019 Global Burden of Disease (GBD) study [1]. The link to the specific query producing these values is available [here](https://vizhub.healthdata.org/gbd-results?params=gbd-api-2019-permalink/425a894085dc3d56f2afc765182f8b06).

### National Health Interview Survey Data
The full National Health Interview Survey (NHIS) database was manually curated to only include the prevalence values for the diseases in the template list, the spreadsheet is availabel [here](https://docs.google.com/spreadsheets/d/16TYXlwe9Q-yiLDa5bOz0UoleOK15D5w9BFJKXVIaFnM/edit?usp=sharing). 

## Data Processing
Data is combined using the `process_rwd.ipynb` notebook to create a single CSV file called `real_world_data.csv`. 

## To Do
- Parkinson = duplicate with PD --> remove parkinson from logit+ counts keep PD
- Covid name on logits wrong-> re-run with covid-19
- spotting problems meant to be menstruuation -> remove from logits and counts
- mi and mnd logits should be re-run with full name or capitalized at least
- gastritis vs acute gastritis -> remove acute and keep gastric problems
- Tendinitis duplicate with achilles tendinitis -> keep achilles

_[1] Global Burden of Disease Collaborative Network. Global Burden of Disease Study 2019 (GBD 2019) Results. Seattle, United States: Institute for Health Metrics and Evaluation (IHME), 2020. Available from https://vizhub.healthdata.org/gbd-results/._

