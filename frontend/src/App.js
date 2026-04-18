import { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [file, setFile] = useState(null);
  const [documents, setDocuments] = useState([]);
  const [chats, setChats] = useState([]);
  const [currentChat, setCurrentChat] = useState(null);
  const [loading, setLoading] = useState(false);

  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chats]);

  // Upload PDF
  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://127.0.0.1:8000/upload", formData);

    setDocuments((prev) => [...prev, res.data]);

    alert("PDF uploaded!");
  };

  // Create new chat
  const createNewChat = () => {
    if (!documents.length) {
      alert("Upload a PDF first!");
      return;
    }

    const newChat = {
      name: `Chat ${chats.length + 1}`,
      messages: [],
      index: documents[documents.length - 1].index,
    };

    setChats([...chats, newChat]);
    setCurrentChat(chats.length);
  };

  // Ask question
  const handleAsk = async () => {
    if (currentChat === null) {
      alert("Select a chat!");
      return;
    }

    const updatedChats = [...chats];
    const chat = updatedChats[currentChat];

    console.log("Using index:", chat.index);

    chat.messages.push({ role: "user", text: question });
    setChats(updatedChats);
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/ask", {
        question,
        index: chat.index,
      });

      chat.messages.push({
        role: "bot",
        text: res.data.answer,
        sources: res.data.sources,
      });

      setChats([...updatedChats]);
    } catch (err) {
      console.error(err);
      alert("Backend error");
    }

    setLoading(false);
    setQuestion("");
  };

  return (
    <div className="app">

      {/* Sidebar */}
      <div className="sidebar">
        <button onClick={createNewChat}>+ New Chat</button>

        <h3>Chats</h3>
        {chats.map((chat, i) => (
          <div
            key={i}
            className="chat-item"
            onClick={() => setCurrentChat(i)}
          >
            {chat.name}
          </div>
        ))}

        <h3>Documents</h3>
        {documents.map((doc, i) => (
          <div
            key={i}
            className="chat-item"
            onClick={() => {
              if (currentChat === null) {
                alert("Select a chat first!");
                return;
              }

              const updatedChats = [...chats];
              updatedChats[currentChat].index = doc.index;

              setChats(updatedChats);
            }}
            style={{
              background:
                currentChat !== null &&
                chats[currentChat].index === doc.index
                  ? "#444"
                  : "transparent",
            }}
          >
            {doc.name}
          </div>
        ))}
      </div>

      {/* Main */}
      <div className="main">

        <div className="upload">
          <input type="file" onChange={(e) => setFile(e.target.files[0])} />
          <button onClick={handleUpload}>Upload PDF</button>
        </div>

        <div className="chat-container">
          {currentChat !== null &&
            chats[currentChat].messages.map((msg, i) => (
              <div key={i} className={`message ${msg.role}`}>
                <div>{msg.text}</div>

                {msg.sources && (
                  <div className="sources">
                    {msg.sources.map((s, idx) => (
                      <div key={idx}>- {s}</div>
                    ))}
                  </div>
                )}
              </div>
            ))}

          {loading && <div className="message bot">Thinking...</div>}
          <div ref={chatEndRef} />
        </div>

        <div className="input-container">
          <input
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleAsk()}
            placeholder="Ask something..."
          />
          <button onClick={handleAsk}>➤</button>
        </div>
      </div>
    </div>
  );
}

export default App;