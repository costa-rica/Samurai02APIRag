import os, json, argparse
from sentence_transformers import SentenceTransformer
import faiss
from app_package._common.config import config

def retrieve(query: str, k: int, embed_model="sentence-transformers/all-MiniLM-L6-v2", debug=False):
    index_path = os.path.join(config.PATH_TO_RAG_INDEX, "faiss.index")
    docs_json = os.path.join(config.PATH_TO_RAG_INDEX, "docs.json")
    
    index = faiss.read_index(index_path)
    with open(docs_json) as f:
        docs = json.load(f)
    model = SentenceTransformer(embed_model)
    q_emb = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    scores, idxs = index.search(q_emb, k)
    ctx = [docs[i] for i in idxs[0]]
    if debug:
        print("DEBUG: Retrieved documents:")
        for rank, (i, s) in enumerate(zip(idxs[0], scores[0])):
            print(f"  [{rank}] idx={i} score={float(s):.4f} :: {docs[i]}")
    return ctx

def build_prompt(question: str, context_snippets):
    system_msg = (
        "You are a concise analyst. Use ONLY the provided context when answering. "
        "If the context is insufficient, say so explicitly."
    )
    ctx_blob = "\n".join(f"- {c}" for c in context_snippets)
    user_msg = (
        f"Question: {question}\n\n"
        f"Context (sleep rows):\n{ctx_blob}\n\n"
        "Answer with dates and numbers when possible."
    )

    # Copy-ready block you can paste into any chat model
    prompt = (
        "### SYSTEM\n"
        f"{system_msg}\n\n"
        "### USER\n"
        f"{user_msg}"
    )
    return prompt

def create_prompt_manager(question: str, k: int, debug=False):
    parser = argparse.ArgumentParser(description="Build a copy-paste RAG prompt from your FAISS index.")
    parser.add_argument("question", help="Your question to ask the model.")
    parser.add_argument("-k", type=int, default=7, help="How many context chunks to retrieve.")
    parser.add_argument("--debug", action="store_true", help="Print retrieved chunks for inspection.")
    # args = parser.parse_args()

    ctx = retrieve(question, k=k, debug=debug)
    prompt = build_prompt(question, ctx)

    # print("\n----- COPY THIS PROMPT INTO YOUR CHAT MODEL -----\n")
    # print(prompt)
    # print("\n----- END PROMPT -----\n")
    return prompt
