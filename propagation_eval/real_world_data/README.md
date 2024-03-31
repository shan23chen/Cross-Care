# Real World Data
Prevalence estimates for each disease were manually curated and cross-validated by a Certified Physician.

Prevalence was preferably collected, however if not present then Incidence values were collected in their place. 

Gender Prevalence for X diseases was collected via the 2019 Global Burden of Disease (GBD) study [1], and the link to the specific query producing these values is available [here](https://vizhub.healthdata.org/gbd-results?params=gbd-api-2019-permalink/425a894085dc3d56f2afc765182f8b06).

The remaining values for Gender and all Racial values were manually curated from government statistics and peer-reviewed publications. The link to these values is available [here](https://docs.google.com/spreadsheets/d/1xF_BJi2Fw4g75QlyD5dxSHpbyad3B-rGSpRk2igDc30/edit?usp=sharing).

## To Do
- Parkinson = duplicate with PD --> remove parkinson from logit+ counts keep PD
- Covid name on logits wrong-> re-run with covid-19
- spotting problems meant to be menstruuation -> remove from logits and counts
- mi and mnd logits should be re-run with full name or capitalized at least
- gastritis vs acute gastritis -> remove acute and keep gastric problems
- Tendinitis duplicate with achilles tendinitis -> keep achilles

_[1] Global Burden of Disease Collaborative Network. Global Burden of Disease Study 2019 (GBD 2019) Results. Seattle, United States: Institute for Health Metrics and Evaluation (IHME), 2020. Available from https://vizhub.healthdata.org/gbd-results/._

