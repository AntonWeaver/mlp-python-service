# Project: Full Name Extraction with OpenAI (via Caila)

This project extracts full names (ФИО) from provided text using OpenAI GPT-3.5, and returns the results as structured entities with metadata, such as name position and type. It’s designed to handle both Russian and English names using a combination of API requests and regular expression processing.

## Features
Text processing: Accepts multiple text inputs to process and extract full names.
Name extraction: Identifies and extracts both English and Russian full names (ФИО) using OpenAI GPT-3.5 model.
Structured output: Returns a structured response containing extracted names, their positions within the text, and metadata about the entity.
API integration: Utilizes OpenAI API to handle natural language processing tasks.
Cloud-ready: Can be deployed on MLP Cloud using MLP SDK.

## How It Works
- Input: You provide a list of texts via a PredictRequest model.
- API Request: The text is sent to OpenAI GPT-3.5, which returns a response containing potential names.
- Name Extraction: A regular expression is used to extract full names (both English and Russian) from the API response.
- Entity Creation: Extracted names are stored as entities with metadata such as their position in the text.
- Output: The final output is a structured PredictResponse containing all the extracted entities for each input text.

## Service Accuracy Evaluation (Caila) with Jupyter Notebook
This project includes a Jupyter Notebook (service_analysis.ipynb) that demonstrates the evaluation of the service's accuracy in extracting full names (ФИО) using the Caila API.
- Dataset Used
For accuracy evaluation, we used the NERUS dataset, which can be found at NERUS GitHub.
- Evaluation Metrics. 
We evaluate the service based on three key metrics: Recall, Precision, F1 Score.
We compute Macro-averaged metrics, meaning that we calculate the metrics for each pair (list of correct names and predicted names) and then output the average values.
- Common Model Errors & thoughts

## Requirements
Python 3.8+
mlp_sdk for hosting and managing cloud services
Caila API access

## About Caila
> Caila is a platform for hosting microservices based on ML models.
> It is a powerful tool that can cover every aspect of your solution’s lifecycle, from model training and QA to deployment and monitoring.

[Create a new project](https://github.com/new?template_name=mlp-python-service-template&template_owner=just-ai) from this template to start developing a service of your own!

If you would like to learn more about Caila, check out our official [documentation](https://docs.caila.io/).

## License

This project is licensed under Apache License 2.0.
