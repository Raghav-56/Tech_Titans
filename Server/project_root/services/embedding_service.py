from sentence_transformers import SentenceTransformer
from database.chroma_db import collection

model = SentenceTransformer("all-MiniLM-L6-v2")


def process_text(text):
    """Process text into sentences"""
    print("Tokenizing sentences...")
    sentences = nltk.sent_tokenize(text)
    print(f"Processed {len(sentences)} sentences.")
    return sentences


async def store_in_chromadb(sentences, document_name):
    """Store sentences in ChromaDB with progress indicator and batch processing"""
    print(f"Storing {len(sentences)} sentences in ChromaDB...")
    for i in range(0, len(sentences), BATCH_SIZE):
        batch = sentences[i : i + BATCH_SIZE]
        await asyncio.to_thread(
            collection.add,
            documents=batch,
            metadatas=[{"source": document_name} for _ in batch],
            ids=[f"{document_name}_{j}" for j in range(i, i + len(batch))],
        )
        progress_bar(min(i + BATCH_SIZE, len(sentences)), len(sentences))
    print("\nStorage in ChromaDB complete.")
