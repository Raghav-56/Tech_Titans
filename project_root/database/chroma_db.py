import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./chroma_db")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = None


def init_db():
    global collection
    collection = client.get_or_create_collection(
        name="pdf_embeddings", embedding_function=sentence_transformer_ef
    )
