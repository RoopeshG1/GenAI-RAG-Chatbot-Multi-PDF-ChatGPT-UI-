from app.rag_pipeline import RAGPipeline
from app.vector_store import VectorStore

# Step 1: Load document
pipeline = RAGPipeline()
docs = pipeline.load_documents("../data/sample.txt")

# Step 2: Split
split_docs = pipeline.split_documents(docs)

# Step 3: Store
store = VectorStore()
store.create_vector_store(split_docs)

# Step 4: Query
query = "What is this document about?"
results = store.search(query)

for r in results:
    print(r.page_content)