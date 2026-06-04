import sys
import os
import chromadb
from sentence_transformers import SentenceTransformer

sys.stdout.reconfigure(encoding="utf-8")

from ingest import load_and_chunk_all

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "uw_guide"
EMBED_MODEL = "all-MiniLM-L6-v2"


def build_vectorstore():
    """Embed all chunks and persist them to ChromaDB. Safe to re-run — clears and rebuilds."""
    print("Loading and chunking documents...")
    chunks = load_and_chunk_all()
    print(f"Total chunks: {len(chunks)}")

    print(f"Loading embedding model: {EMBED_MODEL}")
    model = SentenceTransformer(EMBED_MODEL)

    print("Embedding chunks...")
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_list=True)

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    ids = [f"{c['source']}__chunk{c['chunk_index']}" for c in chunks]
    metadatas = [{"source": c["source"], "chunk_index": c["chunk_index"]} for c in chunks]

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas,
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB at ./{CHROMA_DIR}/")
    return collection


def get_collection():
    """Load the persisted ChromaDB collection."""
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    return client.get_collection(COLLECTION_NAME)


def retrieve(query: str, k: int = 5) -> list[dict]:
    """
    Return the top-k most relevant chunks for a query.

    Each result dict contains:
        text        — the chunk content
        source      — source filename
        chunk_index — position of chunk within its document
        score       — cosine distance (lower = more similar)
    """
    model = SentenceTransformer(EMBED_MODEL)
    query_embedding = model.encode(query, convert_to_list=True)

    collection = get_collection()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    output = []
    for text, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        output.append({
            "text": text,
            "source": meta["source"],
            "chunk_index": meta["chunk_index"],
            "score": round(dist, 4),
        })
    return output


if __name__ == "__main__":
    if not os.path.exists(CHROMA_DIR):
        build_vectorstore()
    else:
        print(f"ChromaDB already exists at ./{CHROMA_DIR}/ — skipping rebuild.")
        print("Delete the folder and re-run to rebuild.\n")

    query = "what are the most recommended cheap food spots on the Ave near UW?"
    print(f"\nQuery: '{query}'\n")
    results = retrieve(query, k=5)
    for i, r in enumerate(results, 1):
        print(f"[{i}] {r['source']} | chunk {r['chunk_index']} | score {r['score']}")
        print(r["text"][:300])
        print()
