import { useState } from "react";
import axios from "axios";

export default function Chat() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [sessionId] = useState(() => {
    const saved = localStorage.getItem("techvalley_session_id");
    if (saved) return saved;

    const generated =
      crypto.randomUUID?.() || `session-${Date.now()}-${Math.random()}`;

    localStorage.setItem("techvalley_session_id", generated);
    return generated;
  });

  const sendMessage = async () => {
    const trimmed = message.trim();
    if (!trimmed) return;

    const userMsg = {
      role: "user",
      content: trimmed
    };

    setMessage("");
    setMessages((prev) => [...prev, userMsg]);

    try {
      const res = await axios.post("http://localhost:8000/chat", {
        message: trimmed,
        session_id: sessionId
      });

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: res.data.response
        }
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Sorry, I couldn't reach the backend right now."
        }
      ]);
    }
  };

  return (
    <section className="chat-page">
      <div className="chat-shell">
        <div className="chat-header">
          <h2>Tessa by Technovalley</h2>
        </div>

        <div className="chat-body">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`chat-message ${msg.role === "user" ? "user" : "assistant"}`}
            >
              <div className="chat-message-text">{msg.content}</div>
            </div>
          ))}
        </div>

        <div className="chat-input-row">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask Tessa anything..."
            onKeyDown={(e) => {
              if (e.key === "Enter") sendMessage();
            }}
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </section>
  );
}
