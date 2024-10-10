import openai
import os
from typing import Optional

class TrainedModelChatbot:
    def __init__(self, api_key: str, model_name: Optional[str] = "text-davinci-003", fine_tuned_model: Optional[str] = None):
        """
        Initialize the TrainedModelChatbot with the API key, model name, and optional fine-tuned model.
        :param api_key: The OpenAI API key for authentication
        :param model_name: The GPT model to be used for answering questions (e.g., "text-davinci-003")
        :param fine_tuned_model: The fine-tuned model ID to use for customized responses
        """
        self.api_key = api_key
        self.model_name = fine_tuned_model if fine_tuned_model else model_name
        self.conversation_history = ""
        openai.api_key = self.api_key

    def ask_question(self, question: str) -> str:
        """
        Get an answer from the chatbot for a given question, considering the conversation history.
        :param question: The question to be asked
        :return: The answer provided by the model
        """
        self.conversation_history += f"Human: {question}\n"
        try:
            response = openai.Completion.create(
                engine=self.model_name,
                prompt=self.conversation_history + "AI:",
                max_tokens=150,
                stop=["\n", "Human:", "AI:"]
            )
            answer = response.choices[0].text.strip()
            self.conversation_history += f"AI: {answer}\n"
            return answer
        except openai.error.OpenAIError as e:
            return f"Error: Failed to get a response. Details: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"

    def reset_conversation(self) -> None:
        """
        Reset the conversation history.
        """
        self.conversation_history = ""

if __name__ == "__main__":
    # Set the environment variables or replace with your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
    fine_tuned_model_id = "ft-xxxxxxxxxxxxxxxxxxxxxxxx"

    # Create an instance of TrainedModelChatbot
    chatbot = TrainedModelChatbot(api_key, fine_tuned_model=fine_tuned_model_id)

    # Example usage
    question = "What are the benefits of exercise?"
    answer = chatbot.ask_question(question)
    print(f"Question: {question}\nAnswer: {answer}")

    follow_up_question = "How often should I exercise?"
    follow_up_answer = chatbot.ask_question(follow_up_question)
    print(f"Question: {follow_up_question}\nAnswer: {follow_up_answer}")