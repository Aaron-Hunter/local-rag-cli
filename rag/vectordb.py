import chromadb
import os

class VectorDB:
    def __init__(self):
        current_dir = os.getcwd()
        self.client = chromadb.PersistentClient(path=f"{current_dir}/db")
        self.collection = self.client.get_or_create_collection("rag_docs")

    def add(self, ids, texts, embeddings, metadatas):
        self.collection.add(documents=texts, ids=ids, embeddings=embeddings, metadatas=metadatas)

    def query(self, query_embedding, k=5):
        results = self.collection.query(query_embeddings=[query_embedding], n_results=k)
        return results["documents"][0]