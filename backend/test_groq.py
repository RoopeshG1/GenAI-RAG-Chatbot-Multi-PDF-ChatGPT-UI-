from app.rag_pipeline import RAGPipeline

rag = RAGPipeline()

# Load your file
rag.ingest("data/text.pdf")

while True:
    query = input("\nAsk something: ")

    if query.lower() == "exit":
        break

    response = rag.query(query)

    print("\n💡 Answer:\n", response)