import sys
import random

sys.stdout.reconfigure(encoding="utf-8")

from ingest import load_and_chunk_all

chunks = load_and_chunk_all()
print(f"Total chunks: {len(chunks)}\n")

for c in random.sample(chunks, min(5, len(chunks))):
    print(f"--- [{c['source']} | chunk {c['chunk_index']}] ---")
    print(c["text"])
    print()
