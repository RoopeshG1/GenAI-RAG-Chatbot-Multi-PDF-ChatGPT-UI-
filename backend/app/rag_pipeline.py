import uuid
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.vector_store import VectorStore
from app.llm import generate_response


class RAGPipeline:
    def __init__(self):
        self.store = VectorStore()

    def load_documents(self, file_path):
        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path)

        return loader.load()

    def split_documents(self, docs):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
        return splitter.split_documents(docs)

    def ingest(self, file_path):
        unique_id = str(uuid.uuid4())[:8]
        index_path = f"faiss_index_{unique_id}"

        docs = self.load_documents(file_path)
        split_docs = self.split_documents(docs)

        self.store.create_vector_store(split_docs)
        self.store.save(index_path)

        return index_path

    def load_index(self, index_path):
        from app.vector_store import VectorStore

        # 🔥 IMPORTANT FIX
        self.store = VectorStore()
        self.store.load(index_path)

        print("📂 Loaded index:", index_path)

    def query(self, question):
        docs = self.store.search(question)

        context = "\n".join([doc.page_content for doc in docs])

        answer = generate_response(context, question)

        sources = [doc.page_content[:100] for doc in docs]

        return {"answer": answer, "sources": sources}