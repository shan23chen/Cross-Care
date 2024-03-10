<!-- exclude_docs -->
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE.txt)
[![Arxiv](https://img.shields.io/badge/Arxiv-pending-red)](https://github.com/Gallifantjack/Cross-Care)

<!-- exclude_docs_end -->

<!-- exclude_docs -->
> **⚗️ Status:** This project is still in *alpha*, and may change without warning.  
<!-- exclude_docs_end -->
<!-- include_docs
:::{important}
**Status:** This project is still in *alpha*, and the API may change without warning.  
:::
include_docs_end -->


# Cross-Care 

Cross-Care is a project that compares the co-occurrences of medical terms with demographic terms in pretraining data and investigates the downstream effects of these co-occurrences on the biases of language models trained on them. The project is divided into three main parts: co-occurrence analysis, logits analysis, and propagation evaluation. The results of these analyses are then visualized in a web application.


## Overview
```
Cross-Care/
│
├── co_occurrence_generate  # contains the code for co-occurrence analysis
│   ├── README.md           # contains instructions on how to run the co-occurrence analysis
│   
├── co_occurrence_results
│   ├── output/pile/           # Results specific to the Pile dataset
│   
├── logits_generate
│   ├── README.md           # contains instructions on how to run the logits analysis
│
├── logits_results
│   ├── api/               # Results specific to the API model
│   ├── hf/                # Results specific to the Hugging Face model
│   ├── hf_tf/             # Results specific to the Hugging Face model with True/False setting
│
├── propagation_eval
│   ├── README.md           # contains instructions on how to run the propagation evaluation
│
├── web_app
│   ├── README.md           # contains instructions on how to run the web app
│
├── .env                    # contains environment variables including API keys
├── .gitignore              # contains files and directories to be ignored by git
├── LICENSE                 # contains the license for this project
├── README.md               # contains the main documentation for this project
```

### Co-occurrence Analysis

The co-occurrence analysis is performed using ...
- Datasets
  - Those included ...
  - Can be downloaded ...
- Keyword dictionaries
- Windows
- Filter
- Co-occurrence Analysis
- Results are saved in the co_occurrence_results folder.

Details on how to run the co-occurrence analysis can be found in the [co_occurrence_generate/README.md](co_occurrence_generate/README.md) file.

### Logits Analysis
The logits analysis is performed using...
- models
- api vs hf 
- languages, tf vs seq
- round robin templates
- Results are saved in the logits_results folder.

Details on how to run the logits analysis can be found in the [logits_generate/README.md](logits_generate/README.md) file.

### Propagation Evaluation
The propagation evaluation is performed using...
- Joining the co-occurrence and logits results
- comparing windows, models, sizes, etc.
- Rank based approach
- Results are saved in the propagation_eval folder.

Details on how to run the analysis for propagation evaluation can be found in the [propagation_eval/README.md](propagation_eval/README.md) file.


### Web App

The web app is a fully functional web application that allows users to interact with the data and results of the project. The web app is built using Next.js, hosted on Vercel, and the backend is hosted on Heroku. The web app is accessible at [cross-care.vercel.app](https://cross-care.vercel.app).


## Setting Up Environment 

### Docker



### Managing API Keys

To securely manage your API keys, you can use environment variables. Follow these steps to set up the environment variables for this project:

1. **Create a .env file:**

In the root directory of your project, create a file named `.env`. Add the following lines to this file:

```md
GPT4V_KEY=your_gpt4v_key_here
OPENAI_KEY=your_openai_key_here
```

Replace `your_gpt4v_key_here` and `your_openai_key_here` with your actual API keys.

2. **Load the variables in your Python script:**

If you need these keys then at the beginning of your Python script, add the following code to load and access the environment variables:

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
gpt4v_key = os.getenv('GPT4V_KEY')
openai_key = os.getenv('OPENAI_KEY')
```

With these steps, your API keys will be securely stored in the .env file and easily accessible in your Python script.


## Contributing
Contributions to improve the code or add additional functionalities are welcome! Please ensure to follow the existing code structure and comment appropriately.

## Acknowledgements


## License
