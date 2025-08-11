from flask import Blueprint
from flask import request
# from flask import render_template, current_app, send_from_directory
import os
from app_package._common.utilities import custom_logger
from app_package._modules.rag_build_index import build_index_for_rag
from app_package._modules.rag_build_prompt import create_prompt_manager

logger_bp_rag = custom_logger('bp_rag.log')
bp_rag = Blueprint('bp_rag', __name__)
# how do I add a prefix to all routes in this blueprint?
bp_rag.url_prefix = '/rag'


# GET /rag/ping
@bp_rag.get("/ping")
def ping():
    logger_bp_rag.info("-- in rag/ping route --")
    print("-- in rag/ping route --")
    return {"message": "pong"}

# GET /rag/build_index
@bp_rag.get("/build-index")
def build_index():
    logger_bp_rag.info("-- in rag/build_index route --")
    print("-- in rag/build_index route --")
    build_index_for_rag()
    return {"ok": True}

@bp_rag.post("/build-prompt")
def build_prompt():
    # Parse JSON body
    data = request.get_json()
    if not data:
        return {"error": "Missing JSON body"}, 400

    # Validate required fields
    question = data.get("question")
    k = data.get("k")
    if question is None or k is None:
        return {"error": "JSON body must contain 'question' and 'k'"}, 400

    # Optional: ensure k is an integer
    try:
        k = int(k)
    except ValueError:
        return {"error": "'k' must be an integer"}, 400

    logger_bp_rag.info(f"-- in rag/build-prompt route -- question={question}, k={k}")

    # Call your RAG prompt builder
    prompt = create_prompt_manager(question, k)

    logger_bp_rag.info(f"-- in rag/build-prompt route -- prompt={prompt}")

    return {
        "ok": True,
        # "question": question,
        # "k": k,
        "prompt": prompt  # assuming create_prompt_manager returns a string or dict
    }