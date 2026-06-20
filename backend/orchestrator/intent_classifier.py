from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")


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
