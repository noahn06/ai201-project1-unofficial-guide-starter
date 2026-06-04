import os
import re
import sys
import tiktoken

sys.stdout.reconfigure(encoding="utf-8")

DOCUMENTS_DIR = "documents"
CHUNK_SIZE = 300
OVERLAP = 50

def clean_text(raw: str) -> str:
    # Remove deleted/moderated content blocks
    raw = re.sub(r'\[deleted\].*?(?=\n\n|\Z)', '', raw, flags=re.DOTALL)
    raw = re.sub(r'Comment deleted by user.*?(?=\n\n|\Z)', '', raw, flags=re.DOTALL)
    raw = re.sub(r'Comment removed by moderator.*?(?=\n\n|\Z)', '', raw, flags=re.DOTALL)
    raw = re.sub(r'This post was mass deleted and anonymized with Redact.*?(?=\n\n|\Z)', '', raw, flags=re.DOTALL)
    raw = re.sub(r'Sorry, this post was deleted by the person who originally posted it\.', '', raw)

    # Remove all usernames and avatar lines
    raw = re.sub(r'u/\S+', '', raw)                                    # u/username anywhere
    raw = re.sub(r'\S+ avatar\b', '', raw)                             # "username avatar" combos
    raw = re.sub(r'\bavatar\b', '', raw)                               # orphaned "avatar" tokens
    raw = re.sub(r'\bOP\b', '', raw)

    # Strip flair lines FIRST (before timestamps are removed) — flair always appears
    # on its own line immediately after a timestamp line (e.g. "2y ago" or "Edited 2y ago")
    timestamp_re = re.compile(r'^(?:Edited\s+)?\d+\S*\s+ago$')
    lines = raw.splitlines()
    cleaned_lines = []
    skip_next = False
    for line in lines:
        if skip_next and line.strip():
            skip_next = False
            continue  # flair line — drop it
        if timestamp_re.match(line.strip()):
            skip_next = True
        cleaned_lines.append(line)
    raw = '\n'.join(cleaned_lines)

    # Remove Reddit scaffolding: upvote/downvote counts, vote buttons, timestamps
    raw = re.sub(r'\bUpvote\b', '', raw)
    raw = re.sub(r'\bDownvote\b', '', raw)
    raw = re.sub(r'\bReply\b', '', raw)
    raw = re.sub(r'\bShare\b', '', raw)
    raw = re.sub(r'^\s*\d+\s*$', '', raw, flags=re.MULTILINE)       # standalone vote counts
    raw = re.sub(r'\bEdited\s+\d+\S*\s+ago\b', '', raw)             # "Edited 2y ago"
    raw = re.sub(r'\b\d+\S*\s+ago\b', '', raw)                      # "2y ago", "3mo ago", "10d ago"
    raw = re.sub(r'\d+ more repl(?:y|ies)', '', raw)
    raw = re.sub(r'Go to comments', '', raw)
    raw = re.sub(r'Sort by:.*?(?=\n)', '', raw)
    raw = re.sub(r'Search Comments.*?(?=\n)', '', raw)
    raw = re.sub(r'Expand comment search.*?(?=\n)', '', raw)
    raw = re.sub(r'Comments Section', '', raw)

    # Remove bullet separators (reddit comment metadata dots)
    raw = re.sub(r'\s*•\s*', ' ', raw)

    # Remove bare Reddit username tokens.
    # Usernames contain underscore/hyphen separators or end with digits — never plain dictionary words.
    # Pattern covers: Snake_Case123, camelCase99, word-hyphen99, MixedCase_stuff
    raw = re.sub(r'\b[A-Za-z][A-Za-z0-9]*(?:[_\-][A-Za-z0-9]+)+\d*\b', '', raw)  # has separator
    raw = re.sub(r'\b[A-Za-z][A-Za-z0-9]*\d{2,}\b', '', raw)                      # ends in 2+ digits
    # Drop lines that are now empty or only whitespace after username removal
    lines = raw.splitlines()
    raw = '\n'.join(line for line in lines if line.strip())

    # Collapse excessive whitespace
    raw = re.sub(r'\n{3,}', '\n\n', raw)
    raw = re.sub(r'[ \t]+', ' ', raw)

    return raw.strip()


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> list[str]:
    enc = tiktoken.get_encoding("cl100k_base")
    token_ids = enc.encode(text)

    chunks = []
    start = 0
    while start < len(token_ids):
        end = start + chunk_size
        chunk_ids = token_ids[start:end]
        chunks.append(enc.decode(chunk_ids))
        if end >= len(token_ids):
            break
        start = end - overlap

    return chunks


def load_and_chunk_all(documents_dir: str = DOCUMENTS_DIR) -> list[dict]:
    all_chunks = []
    for filename in sorted(os.listdir(documents_dir)):
        if not filename.endswith(".txt"):
            continue
        filepath = os.path.join(documents_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            raw = f.read()
        cleaned = clean_text(raw)
        chunks = chunk_text(cleaned)
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "source": filename,
                "chunk_index": i,
                "text": chunk,
            })
    return all_chunks


if __name__ == "__main__":
    chunks = load_and_chunk_all()
    print(f"Total chunks: {len(chunks)}\n")

    # Verification: print first 5 chunks from uw_reddit_dorms.txt
    dorm_chunks = [c for c in chunks if c["source"] == "uw_reddit_dorms.txt"]
    print(f"uw_reddit_dorms.txt -> {len(dorm_chunks)} chunks\n")
    for c in dorm_chunks[:5]:
        print(f"--- Chunk {c['chunk_index']} ---")
        print(c["text"])
        print()
