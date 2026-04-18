from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_text(file_path):
    loader = TextLoader(file_path)
    return loader.load()

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()