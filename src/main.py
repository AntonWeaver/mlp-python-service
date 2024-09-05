from mlp_sdk.abstract import Task
from mlp_sdk.hosting.host import host_mlp_cloud
from mlp_sdk.transport.MlpServiceSDK import MlpServiceSDK
from pydantic import BaseModel
import requests
import re


# Model for the prediction request, which will contain a list of texts
class PredictRequest(BaseModel):
    texts: list

    def __init__(self, texts: list):
        # Initialize the request with the provided texts
        super().__init__(texts=texts)


# Model for representing the span of an entity (start and end indexes)
class EntitySpan(BaseModel):
    start_index: int
    end_index: int


# Model for representing an entity, such as a name
class Entity(BaseModel):
    value: str
    entity_type: str
    span: EntitySpan
    entity: str
    source_type: str = "SLOVNET"  # Default source type is SLOVNET


# Model for representing a list of entities
class EntitiesList(BaseModel):
    entities: list[Entity]


# Model for the prediction response, containing a list of entities lists
class PredictResponse(BaseModel):
    entities_list: list[EntitiesList]


# Class that represents the action performed, inheriting from Task
class SimpleAction(Task):
    def __init__(self, config: BaseModel, service_sdk: MlpServiceSDK = None) -> None:
        # Initialize the base class with configuration and optional SDK
        super().__init__(config, service_sdk)

    # Main function for performing the prediction
    def predict(self, data: PredictRequest, config: BaseModel) -> PredictResponse:
        # Request to extract a full name via OpenAI API
        url = 'https://caila.io/api/adapters/openai/chat/completions'
        headers = {
            'Authorization': 'API-KEY', #YOUR CAILA API-KEY
            'Content-Type': 'application/json'
        }

        # Convert sentences into one text to send in a request
        text_input = " ".join(data.texts)

        # Form the request body for the OpenAI API
        request_data = {
            "model": "just-ai/openai-proxy/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": f"Извлеки все ФИО из следующего текста: {text_input}"}
            ]
        }

        # Send a POST request to the API
        response = requests.post(url, headers=headers, json=request_data)
        response_json = response.json()

        # Processing the response from the model
        choices = response_json.get('choices', [])
        if choices:
            content = choices[0].get('message', {}).get('content', '')

            # NRegular expression to detect names (both English and Russian)
            name_pattern = re.compile(r'\b([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+|[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+|[А-ЯЁ]['
                                      r'а-яё]+)\b')
            names = name_pattern.findall(content)

            # List to store all EntitiesList
            final_entities_list = []

            # Check each text to find matching names
            for text in data.texts:
                entities = []

                # For each name found, we find its indexes in the text
                for name in names:
                    start_index = text.find(name)
                    if start_index != -1:
                        end_index = start_index + len(name)

                        # Create an Entity object with name details
                        entity = Entity(
                            value=name,
                            entity_type="PERSON",
                            span=EntitySpan(
                                start_index=start_index,
                                end_index=end_index
                            ),
                            entity=name
                        )
                        entities.append(entity)

                # Add the list of entities to the final result
                entities_list = EntitiesList(entities=entities)
                final_entities_list.append(entities_list)

            # Return PredictResponse with the resulting list of entities
            return PredictResponse(entities_list=final_entities_list)

        else:
            # If no data is found, return an empty list of entities
            return PredictResponse(entities_list=[])


if __name__ == "__main__":
    # Start the hosting of the SimpleAction class with BaseModel as configuration
    host_mlp_cloud(SimpleAction, BaseModel())
