# 🤖 GenAI RAG Chatbot (Multi-PDF + ChatGPT UI)

A full-stack **Retrieval-Augmented Generation (RAG)** application that allows users to upload multiple PDFs, create chat sessions, and ask context-aware questions using a ChatGPT-like interface.

---

## 🚀 Features

* 📄 Upload **multiple PDFs**
* 💬 Create **multiple chat sessions**
* 🔄 Dynamically switch between documents
* 🧠 Context-aware answers using **RAG (FAISS)**
* ⚡ Fast responses using **Groq LLM**
* 🎨 Clean **ChatGPT-style UI**
* 📌 Source attribution for answers

---

## 🏗️ Architecture

```
Frontend (React)
        ↓
Backend API (FastAPI)
        ↓
RAG Pipeline
   ├── Document Loader (PDF/Text)
   ├── Text Splitter
   ├── FAISS Vector Store
   └── Groq LLM (Inference)
```

---

## 📁 Project Structure

```
genai-chatbot/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── rag_pipeline.py
│   │   ├── vector_store.py
│   │   ├── llm.py
│   ├── data/
│   ├── faiss_index_*
│   ├── .env
│
├── frontend/
│   └── src/
│       ├── App.js
│       ├── App.css
```

---

## ⚙️ Tech Stack

### 🔹 Frontend

* React.js
* Axios
* CSS (ChatGPT-style UI)

### 🔹 Backend

* FastAPI
* LangChain
* FAISS (Vector Database)
* Groq LLM API

---

## 🔑 Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-repo-url>
cd genai-chatbot
```

---

### 2️⃣ Backend Setup

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Run backend:

```
uvicorn app.main:app --reload
```

---

### 3️⃣ Frontend Setup

```
cd frontend
npm install
npm start
```

---

## 🌐 API Endpoints

### 📤 Upload PDF

```
POST /upload
```

Response:

```
{
  "index": "faiss_index_xxxx",
  "name": "file.pdf"
}
```

---

### 💬 Ask Question

```
POST /ask
```

Request:

```
{
  "question": "What is AI?",
  "index": "faiss_index_xxxx"
}
```

Response:

```
{
  "answer": "...",
  "sources": ["..."]
}
```

---

## 🧠 How It Works

1. Upload PDF → Stored in `data/`
2. Text is split into chunks
3. FAISS creates embeddings
4. User asks question
5. Relevant chunks retrieved
6. Groq LLM generates answer using context

---

## ⚡ Key Features Explained

### 🔹 Multi-PDF Support

Each uploaded PDF creates a **unique FAISS index**, allowing independent querying.

### 🔹 Chat History

Each chat session stores:

* Messages
* Associated document index

### 🔹 Dynamic Context Switching

Users can switch documents per chat → ensures correct answers.

---

## 🐞 Common Issues & Fixes

| Issue         | Fix                                |
| ------------- | ---------------------------------- |
| Network Error | Ensure backend is running          |
| Old PDF used  | Check selected document in sidebar |
| Upload fails  | Install `python-multipart`         |

---

## 📌 Future Improvements

* 📊 Store chats in MongoDB
* 🔐 User authentication
* 🌍 Deploy on cloud (Vercel + Render)
* 📚 Combine multiple PDFs in one query
* ⚡ Streaming responses (typing effect)

---

## 📜 License

This project is for educational and personal use.

---

## 🙌 Acknowledgements

* LangChain
* Groq API
* FAISS
* FastAPI
* React

---

## 💡 Author

**Roopesh G.**

---

## ⭐ If you like this project

Give it a ⭐ and share!

---
