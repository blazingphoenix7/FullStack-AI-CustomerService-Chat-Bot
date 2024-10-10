from flask import Flask, request, jsonify
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API Key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")

# Endpoint for single question chatbot
@app.route('/api/single-question', methods=['POST'])
def single_question():
    try:
        data = request.json
        question = data.get("question")
        if not question:
            return jsonify({"error": "Question is required"}), 400

        # Get response from GPT model
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return jsonify({"answer": answer})
    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

# Endpoint for conversational chatbot
@app.route('/api/conversation', methods=['POST'])
def conversation():
    try:
        data = request.json
        question = data.get("question")
        conversation_history = data.get("history", "")
        if not question:
            return jsonify({"error": "Question is required"}), 400

        # Update conversation history and get response from GPT model
        prompt = conversation_history + f"Human: {question}\nAI:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            stop=["\n", "Human:", "AI:"]
        )
        answer = response.choices[0].text.strip()
        conversation_history += f"Human: {question}\nAI: {answer}\n"
        return jsonify({"answer": answer, "history": conversation_history})
    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)