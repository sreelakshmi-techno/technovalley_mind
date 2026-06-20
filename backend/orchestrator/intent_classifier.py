import os

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "llama3")

llm = OllamaLLM(model=MODEL, base_url=OLLAMA_URL)


def classify_intent(query):
    """Use a lightweight LLM classification step before routing."""
    text = (query or "").strip()
    if not text:
        return "GENERAL"

    prompt = f"""
Classify the message into exactly one label:
GREETING, COURSE_QUERY, ADMISSION, PAYMENT, SUPPORT, GENERAL.

Message:
{text}

Return only the label.
"""

    try:
        label = llm.invoke(prompt).strip().upper()
        if label in {"GREETING", "COURSE_QUERY", "ADMISSION", "PAYMENT", "SUPPORT", "GENERAL"}:
            return label
    except Exception:
        pass

    lowered = text.lower()
    if any(word in lowered for word in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]):
        return "GREETING"
    if any(word in lowered for word in ["ai", "course", "program", "recommend", "machine learning", "deep learning", "data science", "nlp"]):
        return "COURSE_QUERY"
    if any(word in lowered for word in ["admission", "apply", "eligibility", "join", "enroll"]):
        return "ADMISSION"
    if any(word in lowered for word in ["payment", "fees", "fee", "emi", "installment", "pay"]):
        return "PAYMENT"
    if any(word in lowered for word in ["login", "password", "technical", "issue", "support", "lms", "portal"]):
        return "SUPPORT"
    return "GENERAL"
