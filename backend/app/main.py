from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.rag_pipeline import RAGPipeline
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = RAGPipeline()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    index = rag.ingest(file_path)

    return {"index": index, "name": file.filename}


@app.post("/ask")
async def ask(query: dict):
    index = query.get("index")

    print("🔥 Using index:", index)

    if not index:
        return {"answer": "No document selected", "sources": []}

    if not os.path.exists(index):
        return {"answer": "Index not found. Upload PDF again.", "sources": []}

    rag.load_index(index)

    return rag.query(query["question"])