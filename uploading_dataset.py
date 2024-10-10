import openai
import os
from typing import Optional

class DatasetUploader:
    def __init__(self, api_key: str, dataset_path: str):
        """
        Initialize the DatasetUploader with the API key and dataset path.
        :param api_key: The OpenAI API key for authentication
        :param dataset_path: Path to the dataset file to be uploaded
        """
        self.api_key = api_key
        self.dataset_path = dataset_path
        openai.api_key = self.api_key

    def upload_dataset(self, purpose: Optional[str] = "fine-tune") -> None:
        """
        Upload a dataset to OpenAI's servers for a specified purpose.
        :param purpose: The purpose for which the dataset is being uploaded (e.g., "fine-tune")
        """
        try:
            with open(self.dataset_path, "rb") as dataset_file:
                response = openai.File.create(
                    file=dataset_file,
                    purpose=purpose
                )
            print(f"Successfully uploaded dataset. File ID: {response['id']}")
        except FileNotFoundError:
            print(f"Error: The file '{self.dataset_path}' was not found.")
        except openai.error.OpenAIError as e:
            print(f"Error: Failed to upload dataset. Details: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Set the environment variables or replace with your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
    dataset_filepath = "data/FAQ_data_cleaned_converted.jsonl"

    # Create DatasetUploader instance and perform upload
    uploader = DatasetUploader(api_key, dataset_filepath)
    uploader.upload_dataset()