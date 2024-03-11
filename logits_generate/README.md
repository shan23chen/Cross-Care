#### Overview
The `logits_generate` folder is designed to facilitate the evaluation of logits from language models, with a focus on health-related data. This suite of tools supports evaluation through both custom APIs and Hugging Face models

#### Contents
- `api_eval_logit.py`: Evaluate logits using a custom API, cohere or openai API are supported.
- `hf_eval_logit.py`: Evaluate logits with Hugging Face's Transformers models.
- `hf_model.py`: Manage Hugging Face model loading and preprocessing.
- `hf_tf_eval_logit.py`: True or false eval on logits level support for evaluating Hugging Face models.
- `templates.py`: Template processing for generating model inputs.
- `disease.py`: Handle disease-related data, possibly for input generation or annotation.
- `api_model.py`: Interface for models accessed via APIs, including loading and inference.
- `run_api_logit_eval.sh`: Shell script to automate API-based logit evaluations.
- `run_hf_logit_eval.sh`: Shell script for executing Hugging Face model evaluations.
- `disease_translations.csv`: Data file with disease information, possibly for localization or reference.

#### Installation

1. **Install Dependencies:**
   Ensure you have Python 3.8+ installed. Then, install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   Note: A `requirements.txt` file must be created listing all dependencies, such as `pandas`, `numpy`, `transformers`, and any other required libraries.

#### Usage

- **API Logit Evaluation:**
  Edit `api_eval_logit.py` to specify your API details, then run:
  ```bash
  python api_eval_logit.py
  ```

- **Hugging Face Logit Evaluation:**
  Use `hf_eval_logit.py` for evaluating logits with a Hugging Face model:
  ```bash
  bash run_hf_logit_eval.sh
  ```

For more detailed instructions on each script, refer to comments within the files.

#### Configuration

Some scripts may require you to set specific parameters or environment variables. These include API keys for `api_eval_logit.py` and model names for `hf_eval_logit.py`. Please review each script's documentation at the top of the file for configuration details.

#### Contributing

Contributions to the `logits_generate` project are welcome! Whether you're fixing a bug, adding a new feature, or improving documentation, please feel free to fork the repository and submit a pull request.