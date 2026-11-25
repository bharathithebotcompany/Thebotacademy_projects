import { useState } from "react";
import api from "../api/client";
import Message from "./Message";

function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const sendQuestion = async () => {
    if (!question.trim() || loading) return;

    // add user message
    setMessages((prev) => [
      ...prev,
      { role: "user", text: question },
    ]);

    setLoading(true);


    try {
      const res = await api.post("/chat", {
        question: question,
      });

      // add assistant response
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: res.data.answer },
      ]);
    } catch (error) {
      console.error("Chat error:", error);

      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: "❌ Something went wrong. Please try again." },
      ]);
    } finally {
      setLoading(false);
      setQuestion("");
    }
  };

  return (
    <div className="p-4 border rounded">
      {/* Messages */}
      <div className="h-64 overflow-y-auto mb-2">
        {messages.map((msg, i) => (
          <Message key={i} role={msg.role} text={msg.text} />
        ))}

        {loading && (
          <Message role="assistant" text="Thinking..." />
        )}
      </div>

      {/* Input */}
      <div className="flex">
        <input
          className="border p-2 flex-1"
          value={question}
          disabled={loading}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask something..."
        />

        <button
          disabled={!question.trim() || loading}
          className="bg-blue-500 disabled:bg-gray-400 text-white p-2 ml-2"
          onClick={sendQuestion}
        >
          {loading ? "..." : "Ask"}
        </button>
      </div>
    </div>
  );
}



export default ChatBox;
