# Customer Service Chatbot with OpenAI and Python

This repository contains the code for a customer service chatbot developed using OpenAI's GPT models and Python. The project includes scripts for setting up various types of chatbot interactions, fine-tuning the model with custom datasets, and deploying a conversational chatbot tailored to specific requirements.

## Repository Contents

- `/data`: Contains the datasets used for chatbot training and fine-tuning.
- `.gitignore`: Specifies the files to be ignored by version control.
- `README.md`: Provides an overview of the project and usage instructions.
- `app.py`: Flask backend to handle chatbot queries.
- `frontend/src/App.js`: React frontend to provide a user-friendly interface for interacting with the chatbot.
- `frontend/src/App.css`: Styling for the React frontend.
- `frontend/Dockerfile`: Dockerfile to build and serve the React frontend.
- `docker-compose.yml`: Container orchestration for running both frontend and backend services.
- `chatbot_singlequestion.py`: A script for a chatbot that responds to individual questions.
- `chatbot_conversation.py`: A script for a chatbot capable of handling continuous conversation.
- `chatbot_conversation_tuned.py`: An advanced version of the chatbot with fine-tuning support for improved responses.
- `datatrained_model.py`: A script for a chatbot that utilizes a fine-tuned model, with conversation tracking capabilities.
- `dataconversionscript.py`: A script to convert data from JSON to JSONL format, used for preparing training datasets.
- `uploading_dataset.py`: A utility to upload training datasets to OpenAI for fine-tuning.
- `training_model.py`: A script to initiate the fine-tuning process for the chatbot using OpenAI's API.

## Setup

To set up the chatbot, clone this repository and install the required dependencies. You will need to obtain an OpenAI API key and ensure Python is installed on your system.

1. Clone the repository:
   ```sh
   git clone https://github.com/blazingphoenix7/FullStack-AI-CustomerService-ChatBot.git
   cd FullStack-AI-CustomerService-ChatBot-main
   ```

2. Install the necessary dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up the environment variable for the OpenAI API key:
   ```sh
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

### Data Conversion

Use `dataconversionscript.py` to convert JSON datasets into JSONL format for fine-tuning:
```sh
python dataconversionscript.py
```
This script reads a JSON file containing FAQ data and converts it into JSONL format, which is required by the OpenAI API for training.

### Upload Dataset

After converting the dataset, use `uploading_dataset.py` to upload the dataset to OpenAI's servers for fine-tuning:
```sh
python uploading_dataset.py
```
Ensure that the dataset is in the correct format and that you have your API key ready.

### Fine-Tune Model

Use `training_model.py` to create a fine-tuning job for the chatbot model:
```sh
python training_model.py
```
This script initiates a fine-tuning job using the uploaded dataset and the specified base model.

### Running Chatbots

1. **Single Question Chatbot**
   
   Use `chatbot_singlequestion.py` for a simple, one-off question-answering chatbot:
   ```sh
   python chatbot_singlequestion.py
   ```
   This chatbot is useful for scenarios where only a single response is required.

2. **Conversational Chatbot**

   Use `chatbot_conversation.py` for a more interactive chatbot experience:
   ```sh
   python chatbot_conversation.py
   ```
   This chatbot keeps track of conversation history, providing more contextually aware responses.

3. **Fine-Tuned Conversational Chatbot**

   Use `chatbot_conversation_tuned.py` for a chatbot that leverages a fine-tuned model to provide highly customized responses:
   ```sh
   python chatbot_conversation_tuned.py
   ```
   This version is ideal for tailored use cases, such as customer service for a specific business domain.

4. **Trained Model Chatbot**

   Use `datatrained_model.py` for a chatbot utilizing a fine-tuned model, with support for conversation reset and continuous interaction:
   ```sh
   python datatrained_model.py
   ```

## Deployment Instructions for Chatbot Application

This section provides a step-by-step guide to deploy the customer service chatbot application using Docker. The deployment includes both the Flask backend and the React frontend, orchestrated using Docker Compose.

### Prerequisites

- **Docker**: Make sure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/get-started).
- **Docker Compose**: Docker Compose should also be installed. It is included with Docker Desktop.
- **OpenAI API Key**: You will need an OpenAI API key to authenticate requests to the chatbot.

### Step 1: Clone the Repository

First, clone the repository containing the project files:

```sh
git clone https://github.com/yourusername/finetuned_chatbot-main.git
cd finetuned_chatbot-main
```

Ensure the directory structure includes both the backend and frontend folders:
- `/app.py` (Backend - Flask)
- `/frontend/src/App.js` (Frontend - React)
- `/frontend/Dockerfile` (Frontend Dockerfile)

### Step 2: Update API Key

Update the **OpenAI API key** in the `docker-compose.yml` file:

```yaml
environment:
  - OPENAI_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual API key.

### Step 3: Build the Docker Images

Use Docker Compose to build the images for both the frontend and backend services. Run the following command from the root of the project directory:

```sh
docker-compose build
```

This command will build both the **Flask backend** and the **React frontend** Docker images.

### Step 4: Run the Containers

After successfully building the Docker images, use Docker Compose to start the containers:

```sh
docker-compose up
```

This command will start both the backend and frontend services. You should see the backend server log messages, confirming it is running on port 5000, and the frontend server on port 3000.

### Step 5: Access the Application

- **Frontend**: Open your web browser and go to [http://localhost:3000](http://localhost:3000). This will open the React frontend where you can interact with the chatbot.
- **Backend**: The backend API runs on port 5000 and can be accessed through [http://localhost:5000](http://localhost:5000) if you want to test API endpoints directly.

### Step 6: Interact with the Chatbot

- Enter your question in the input field on the frontend.
- Click the **Ask** button to send the question to the backend.
- The answer from the chatbot will be displayed below the input field.

You can toggle between **Single Question** and **Conversational Mode** to experience different functionalities of the chatbot.

### Step 7: Stopping the Application

To stop the running containers, press `Ctrl + C` in the terminal window where Docker Compose is running. Alternatively, you can run:

```sh
docker-compose down
```

This command will stop and remove all containers, networks, and volumes created by Docker Compose.

### Notes

- **Environment Variables**: Ensure your API key is kept secure. It is recommended to use environment files (`.env`) for production deployments.
- **Production Deployment**: This setup is for local development and testing. For production, consider using cloud services like AWS, Azure, or GCP for hosting, along with container orchestration platforms like Kubernetes.

### Troubleshooting

- **Docker Build Issues**: If you encounter issues during the Docker build, ensure your dependencies are up to date and there are no syntax errors in the Dockerfiles.
- **API Errors**: If the chatbot is not responding, make sure your OpenAI API key is valid and has sufficient quota.

## Conclusion

Congratulations! You have successfully deployed the chatbot application using Docker and Docker Compose. You can now experiment with different configurations and extend the application to fit your needs.

## Features

- **Custom Training**: Fine-tune the chatbot with your own dataset to make it more relevant to specific domains.
- **Multiple Modes**: Use different chatbot scripts for single-response, conversational, or fine-tuned interactions.
- **Data Conversion**: Easy-to-use script for converting JSON data to JSONL format for model training.

## Requirements
- Python 3.7+
- OpenAI API key
- Dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
