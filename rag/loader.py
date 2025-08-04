import pymupdf
from pathlib import Path

def load_pdfs(folder_path):
    docs = []
    for file_path in Path(folder_path).glob("*.pdf"):
        doc = pymupdf.open(file_path)
        text = "\n".join([page.get_text() for page in doc])
        docs.append({"text": text, "source": str(file_path)})
    return docs

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks