import argparse
from rag.loader import load_pdfs, chunk_text
from rag.embedder import Embedder
from rag.vectordb import VectorDB
from rag.llm import call_llama
from rag.utils import generate_id
from tqdm import tqdm

def index_docs(folder):
    print(f"Indexing documents in {folder}")
    embedder = Embedder()
    vectordb = VectorDB()

    docs = load_pdfs(folder)
    for doc in tqdm(docs):  
        chunks = chunk_text(doc["text"])
        embeddings = embedder.embed(chunks)
        ids = [generate_id() for _ in chunks]
        metadatas = [{"source": doc["source"]} for _ in chunks]
        vectordb.add(ids, chunks, embeddings, metadatas)
    print("Indexing complete")

def query_rag(question, k=5):
    embedder = Embedder()
    vectordb = VectorDB()
    q_embed = embedder.embed([question])[0]
    retrieved_docs = vectordb.query(q_embed, k=k)

    context = "\n---\n".join(retrieved_docs)
    prompt = f"""You are a helpful assistant. Use the following context to answer the question.
    
    Context:
    {context}

    Question:
    {question}

    Answer:"""

    response = call_llama(prompt)
    print("\n Answer:\n")
    print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RAG CLI over PDF folder")
    subparsers = parser.add_subparsers(dest="command")

    index_parser = subparsers.add_parser("index", help="Index documents")
    index_parser.add_argument("--folder", required=True, help="Path to folder containing PDFs")

    query_parser = subparsers.add_parser("query", help="Ask a question")
    query_parser.add_argument("--question", required=True, help="The input question")
    query_parser.add_argument("--topk", type=int, default=5, help="Top K documents to retrieve")

    args = parser.parse_args()

    if args.command == "index":
        index_docs(args.folder)
    elif args.command == "query":
        query_rag(args.question, k=args.topk)