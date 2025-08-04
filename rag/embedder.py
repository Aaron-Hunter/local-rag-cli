from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name="prdev/mini-gte"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        embeddings = self.model.encode(texts)
        return embeddings