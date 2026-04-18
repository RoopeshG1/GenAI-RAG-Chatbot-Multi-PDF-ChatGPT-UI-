from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class VectorStore:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )
        self.db = None

    def create_vector_store(self, docs):
        self.db = FAISS.from_documents(docs, self.embeddings)

    def search(self, query, k=5):
        return self.db.similarity_search(query, k=k)

    def save(self, path):
        self.db.save_local(path)

    def load(self, path):
        self.db = FAISS.load_local(
            path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )