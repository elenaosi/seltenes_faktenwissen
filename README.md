# Evaluating Rare Factual Knowledge in Large Language Models

<p align="center">
  <img src="https://img.shields.io/badge/Semantic%20Search-1f6feb?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Semantic%20Chunking-1f6feb?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NLP%20Pipelines-f97316?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Prompt%20Engineering-6f42c1?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLMs-GPT%20%7C%20Llama%20%7C%20Mistral-22c55e?style=for-the-badge" />
</p>



## About the projekt
This repository contains a modular Python pipeline for the systematic collection, processing, and evaluation of rare factual knowledge in Large Language Models (LLMs). The project was developed as part of a bachelor’s thesis and combines data-driven analysis, semantic methods, and structured prompting strategies to rigorously assess the capabilities of modern language models.

The central focus of the project is to investigate how reliably large language models reproduce rare facts, particularly in comparison to frequently occurring facts, and whether a measurable relationship exists between the frequency of a fact in training data and model performance.
By analyzing factual knowledge in the form of structured (subject, relation, object) triples and evaluating multiple state-of-the-art LLMs, the project aims to provide deeper insight into the limitations, robustness, and behavior of language models in the long tail of knowledge.

## Methodological Approach

1. Data Acquisition & Processing
- Automated collection and preprocessing of large-scale text corpora
- Normalization, filtering, and structuring of unstructured data
- Extraction of factual knowledge represented as (subject, relation, object) triples

2. Semantic Chunking & Semantic Search
- Decomposition of large text corpora into semantically coherent chunks
- Embedding-based similarity search for:
- Identification of relevant textual evidence
- Estimation of factual occurrence frequencies
- Robust differentiation between rare and frequent facts

3. Data Labeling & Fact Frequency Estimation
- Automated labeling of facts based on estimated occurrence frequencies
- Construction of an annotated evaluation dataset
- Quantitative classification of facts according to their degree of rarity

4. Prompt Engineering & Model Querying
- Design of structured prompting strategies
- Generation of controlled model queries to reduce prompt-induced bias
- Collection of model outputs as ranked lists rather than binary answers

5. Evaluation & Analysis
- Performance assessment using multiple evaluation metrics
- Correlation analysis (linear and monotonic) between fact frequency and model performance
- Comparative evaluation of multiple LLMs: GPT-4o, Llama 3.1, Mistral 0.3

## Requirements
- Python 3.9
- pip 24.2
- Ollama Software (is available at https://ollama.com)
```
pip install -r requirements.txt
```

## To repeat the experiment, the following steps must be performed:


- Download the training data set, clean it up, and break it down into smaller parts.
```
python3 load_and_clean_training_data.py
```
> The training data set is available at [https://huggingface.co/datasets/wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia).


- Calculation of frequencies of facts using distant supervision assumption (DSA) (note the comments in the code). 
```
python3 calculate_freq.py
```
> The fact data set is available at the following path: ``` ./datasets/fakt_data_raw ```
> 
> The frequencies already calculated for each relational relationship are available at the following path: ``` ./datasets/fakt_data_freq ```


- Prompting Llama 3.1 and Mistral 0.3 with Ollama (see the notes in the comments in the code).
```
Turn on Ollama software locally
```
```
python3 prompt_response_generator.py
```
> Manually created question templates are available at the following path: ``` ./prompts/close_fragen_template.jsonl ```
> 
> Completed prompts for Llama 3.1 and Mistral 0.3 are available at the following path: ``` ./prompts/prompts_for_llama_and_mistral ```
 
> Responses received from Llama 3.1 to prompts are available at the following path: ``` ./prompting_result/llama_result ```
> 
> Responses received from Mistral 0.3 to prompts are available at the following path: ``` ./prompting_result/mistral_result ```


- Prompting GPT-4o via batch API.
```
export OPENAI_API_KEY="dein_API_KEY“
```
```
python3 gpt_prompt_per_batch.py --file_path "_"
```
> ``` --file_path ```: Path to the JSON file containing the finished batches that will be sent to the API. For example ``` "./prompts/prompts_for_gtp_per_batches/P17_gpt_batches.jsonl" ```

> Completed prompts for GPT-4o are available at the following path: ``` ./prompts/prompts_for_gtp_per_batches ```
```
python3 gpt_prompt_per_batch.py --batch_id "_"
```
> ``` --batch_id ```: ID of the batch to check the status. For example ``` "batch_66f3c6325f0c8190aa207ae42d8fe870" ```
```
python3 gpt_prompt_per_batch.py --file_id "_"  --output_path "_"
```
> ``` --file_id ```: File ID to download results. For example ``` "file-teJF9ChSNXgUv86W5xgyXjky" ```
> 
> ``` --output_path ```: Path where the downloaded file should be saved. For example ``` "./prompting_result/gpt_result" ```

> Responses received to prompts are available at the following path: ``` ./prompting_result/gpt_result ```


- Evaluation of the data obtained by calculating various metrics.
```
python3 metriks.py <model_name>
```
 > Possible variants of the model name:
  >
  >gpt / llama / mistral (to obtain results for all relational relationships individually) 
  >
  >all_gpt / all_llama / all_mistral (to obtain results for all relational relationships together)

> Results that have already been calculated are available via the following paths:
> 
> for GPT-4o ``` ./metrics_result/metrics_gpt.jsonl ```
> 
> for Llama 3.1 ``` ./metrics_result/metrics_llama.jsonl ```
> 
> for Mistral 0.3 ``` ./metrics_result/metrics_mistral.jsonl ```
> 
> for all models across all relational relationships ``` ./metrics_result/metrics_all.jsonl ```
