import openai
import os
from typing import Optional

class ModelTrainer:
    def __init__(self, api_key: str, training_file_id: str, model_name: Optional[str] = "davinci"):
        """
        Initialize the ModelTrainer with the API key, training file ID, and model name.
        :param api_key: The OpenAI API key for authentication
        :param training_file_id: The ID of the training file on OpenAI's servers
        :param model_name: The base model to be used for fine-tuning (e.g., "davinci")
        """
        self.api_key = api_key
        self.training_file_id = training_file_id
        self.model_name = model_name
        openai.api_key = self.api_key

    def fine_tune_model(self) -> None:
        """
        Fine-tune a GPT model using the provided training file.
        """
        try:
            response = openai.FineTune.create(
                training_file=self.training_file_id,
                model=self.model_name
            )
            print(f"Fine-tuning job created. Job ID: {response['id']}")
        except openai.error.OpenAIError as e:
            print(f"Error: Failed to create fine-tune job. Details: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Set the environment variables or replace with your OpenAI API key and training file ID
    api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
    training_file_id = "file-xxxxxxxxxxxxxxxxxxxxxxxx"

    # Create ModelTrainer instance and perform fine-tuning
    trainer = ModelTrainer(api_key, training_file_id)
    trainer.fine_tune_model()