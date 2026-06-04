import sys
import os
from dotenv import load_dotenv
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

from embed import retrieve

MODEL = "llama-3.3-70b-versatile"
TOP_K = 5

SYSTEM_PROMPT = """You are a helpful guide for incoming freshmen / transfer students at the University of Washington Seattle.
Answer the question using ONLY the information provided in the context documents below. Do not be verbose, preferably respond to the query in 2-3 sentences.
If the documents don't contain enough information to answer, say "I don't have enough information on that. Sorry."
Do not provide any reasoning on why you don't have documentation, just say "(No documentation found)"
Do not use any outside knowledge. Cite which document(s) your answer comes from at the end of your response."""


def ask(question: str, k: int = TOP_K) -> dict:
    """
    Returns {"answer": str, "sources": list[str]}
    """
    chunks = retrieve(question, k=k)

    context_parts = []
    for chunk in chunks:
        label = f"[{chunk['source']}, chunk {chunk['chunk_index']}]"
        context_parts.append(f"{label}\n{chunk['text']}")
    context = "\n\n".join(context_parts)

    user_message = f"""Context documents:
{context}

Question: {question}"""

    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.,
    )

    answer = response.choices[0].message.content
    sources = [f"{c['source']} (chunk {c['chunk_index']})" for c in chunks]

    return {"answer": answer, "sources": sources}


if __name__ == "__main__":
    eval_questions = [
        "what does McMahon Hall have that other dorms don't?",
        "what day does school get out for Fall quarter 2026?",
        "what are the most popular things to do near Seattle?",
        "what are the most recommended cheap food spots on the Ave near UW?",
        "what is the best way for out-of-state students to save money on UW tuition?",
        "How can I meet Dubs the Husky the dog mascot of the school?"
    ]

    for q in eval_questions:
        result = ask(q)
        print(f"Q: {q}")
        print(result["answer"])
        print("Sources: " + ", ".join(result["sources"]))
        print("\n" + "=" * 60 + "\n")
