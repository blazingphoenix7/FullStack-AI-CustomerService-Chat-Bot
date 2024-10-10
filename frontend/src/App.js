import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [conversationHistory, setConversationHistory] = useState("");
  const [isConversational, setIsConversational] = useState(false);

  const handleSingleQuestionSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/api/single-question", {
        question,
      });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error("Error fetching response:", error);
      setAnswer("Error: Could not get a response.");
    }
  };

  const handleConversationSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/api/conversation", {
        question,
        history: conversationHistory,
      });
      setAnswer(response.data.answer);
      setConversationHistory(response.data.history);
    } catch (error) {
      console.error("Error fetching response:", error);
      setAnswer("Error: Could not get a response.");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Customer Service Chatbot</h1>
        <div className="chatbot-toggle">
          <label>
            <input
              type="checkbox"
              checked={isConversational}
              onChange={() => {
                setIsConversational(!isConversational);
                setConversationHistory("");
                setAnswer("");
              }}
            />
            Conversational Mode
          </label>
        </div>
        <form onSubmit={isConversational ? handleConversationSubmit : handleSingleQuestionSubmit}>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask a question..."
            required
          />
          <button type="submit">Ask</button>
        </form>
        {answer && (
          <div className="response">
            <strong>Answer:</strong> {answer}
          </div>
        )}
      </header>
    </div>
  );
}

export default App;