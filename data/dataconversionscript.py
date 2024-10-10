import json

class DataConverter:
    def __init__(self, input_file: str, output_file: str):
        """
        Initialize the DataConverter with input and output file paths.
        :param input_file: Path to the input JSON file
        :param output_file: Path to the output JSONL file
        """
        self.input_file = input_file
        self.output_file = output_file

    def convert_to_jsonl(self) -> None:
        """
        Convert JSON data to JSONL format by writing each entry as a separate line in the output file.
        """
        try:
            with open(self.input_file, 'r', encoding='utf-8') as infile:
                data = json.load(infile)
                questions = data.get("questions", [])

            if not questions:
                print(f"Warning: No 'questions' key found or it is empty in {self.input_file}.")

            with open(self.output_file, 'w', encoding='utf-8') as outfile:
                for entry in questions:
                    json.dump(entry, outfile)
                    outfile.write('\n')

            print(f"Successfully converted '{self.input_file}' to '{self.output_file}' in JSONL format.")
        except FileNotFoundError:
            print(f"Error: The file '{self.input_file}' was not found.")
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse JSON. Details: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Define paths for input and output files
    input_filepath = "data/FAQ_data_cleaned.json"
    output_filepath = "data/FAQ_data_cleaned_converted.jsonl"

    # Create DataConverter instance and perform conversion
    converter = DataConverter(input_filepath, output_filepath)
    converter.convert_to_jsonl()