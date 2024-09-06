# Project: Name Extraction with OpenAI (via Caila)

This project extracts full names (ФИО) from provided text using OpenAI GPT-3.5, and returns the results as structured entities with metadata, such as name position and type. It’s designed to handle both Russian and English names using a combination of API requests and regular expression processing.

## Features
- Text processing: Accepts multiple text inputs to process and extract full names.
- Name extraction: Identifies and extracts both English and Russian full names (ФИО) using OpenAI GPT-3.5 model (as Baseline).
- Structured output: Returns a structured response containing extracted names, their positions within the text, and metadata about the entity.
- API integration: Utilizes OpenAI API (Caila API) to handle natural language processing tasks.
- Cloud-ready: Can be deployed on MLP Cloud using MLP SDK.

## How It Works
- Input: You provide a list of texts via a PredictRequest model.
- API Request: The text is sent to OpenAI GPT-3.5, which returns a response containing potential names.
- Name Extraction: A regular expression is used to extract full names (both English and Russian) from the API response.
- Entity Creation: Extracted names are stored as entities with metadata such as their position in the text.
- Output: The final output is a structured PredictResponse containing all the extracted entities for each input text.

## Example Workflow
1. Input
{
  "texts": [
    "Albert Einstein was a theoretical physicist."
  ]
}
2. Output
{
  "entities_list": [
    {
      "entities": [
        {
          "value": "Albert Einstein",
          "entity_type": "PERSON",
          "span": {
            "start_index": 0,
            "end_index": 16
          },
          "entity": "Albert Einstein",
          "source_type": "SLOVNET"
        }
      ]
    }
  ]
}
- entities_list: A list corresponding to each input text.
	- entities: A list of identified entities.
		-value: The extracted full name.
		- entity_type: Type of the entity, e.g., "PERSON".
		- span: Object with start and end indices of the entity in the text.
			- start_index: Starting position of the entity.
			- end_index: Ending position of the entity.
		- entity: Name of the entity.
		- source_type: Method used for extraction, default is "SLOVNET".

## Service Accuracy Evaluation (Caila) with Jupyter Notebook
This project includes a Jupyter Notebook (service_analysis.ipynb) that demonstrates the evaluation of the service's accuracy in extracting full names (ФИО) using the Caila API. Performance is evaluated using the following models: GPT-4o-mini, GPT-3.5-turbo, GPT-3.5-turbo-16k
- Dataset Used
For accuracy evaluation, we used the NERUS dataset, which can be found at NERUS GitHub.
- Performance Evaluation.
Processing Time & Characters Processed per Second
- Evaluation Metrics. 
We evaluate the service based on three key metrics: Recall, Precision, F1 Score.
We compute Macro-averaged metrics, meaning that we calculate the metrics for each pair (list of correct names and predicted names) and then output the average values.
- Common Model Errors & thoughts

## Usage and Deployment
This project is designed to be containerized using Docker and deployed to the Caila service.
To build the service locally, run ./build.sh in the project root. You need to have Docker Engine installed and running.
For more details on deploying Python services with Docker and Caila, refer to the MLP Python Service Template (https://github.com/just-ai/mlp-python-service-template).

## Requirements
Python 3.8+
mlp_sdk for hosting and managing cloud services
Caila API access

## Dependencies
Install required Python packages:
pip install -r requirements.txt

## About Caila
> Caila is a platform for hosting microservices based on ML models.
> It is a powerful tool that can cover every aspect of your solution’s lifecycle, from model training and QA to deployment and monitoring.

[Create a new project](https://github.com/new?template_name=mlp-python-service-template&template_owner=just-ai) from this template to start developing a service of your own!

If you would like to learn more about Caila, check out our official [documentation](https://docs.caila.io/).

## License

This project is licensed under Apache License 2.0.
