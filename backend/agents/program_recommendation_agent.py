import os
import re

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

from agents.base_agent_prompt import PROGRAM_RECOMMENDATION_PROMPT
from rag.retriever import retrieve_documents

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "llama3")

llm = OllamaLLM(model=MODEL, base_url=OLLAMA_URL)

BROCHURE_COURSE_CATALOG = """
Technovalley brochure catalog (use these as the main source for course/program questions):
- PG Diploma in Penetration Testing
- PG Diploma in Digital Forensics and Cyber Defense
- Advanced Diploma in Penetration Testing and Forensics
- Advanced Diploma in Penetration Testing and Security Operations
- PG Diploma in Big Data Analytics
- PG Diploma in Data Science with Machine Learning
- PG Diploma in Artificial Intelligence
- PG Diploma in Cloud Administration and DevOps
- PG Diploma in Networking and System Administration
- Cyber Security international certifications: CEH, OSCP, LPT, and other related certifications
- Emerging Technologies certifications: Data+, PCEP, BCAIP, BCMLP
- IT Infrastructure certifications: Linux+, A+, Cloud+, CCNA, AWS Solution Architect
- Focus areas mentioned in the brochures: Cyber Security Stack, IT Infrastructure Stack, Emerging Technologies Stack
"""


def sanitize_history(history):
    """Keep only recent, non-personal conversation turns to avoid profile leakage."""
    if not history:
        return []

    personal_pattern = re.compile(r"\b(my name is|i am|i'm|myself|user name is)\b", re.IGNORECASE)
    greeting_pattern = re.compile(r"^\s*(hello|hi|hey|good morning|good afternoon|good evening)\b", re.IGNORECASE)

    cleaned = []

    for turn in list(history)[-5:]:
        user_text = "" if turn.get("user") is None else str(turn["user"]).strip()
        assistant_text = "" if turn.get("assistant") is None else str(turn["assistant"]).strip()

        if not user_text and not assistant_text:
            continue

        if personal_pattern.search(user_text) or personal_pattern.search(assistant_text):
            continue

        if greeting_pattern.search(user_text) or greeting_pattern.search(assistant_text):
            continue

        cleaned.append({
            "user": user_text,
            "assistant": assistant_text,
        })

    return cleaned[-3:]


def program_recommendation_agent(query, history):
    retrieved_docs = retrieve_documents(query)

    context = "\n".join([
        doc.page_content
        for doc in retrieved_docs
    ])

    sanitized_history = sanitize_history(history)

    prompt = f"""
    {PROGRAM_RECOMMENDATION_PROMPT}

    Additional guidance:
    - Think first about what the user is actually asking.
    - For course/program questions, prioritize the brochure catalog provided below.
    - Use ONLY the conversation context and the Institutional Context provided below.
    - If the brochure catalog lists specific programs, answer with those exact offerings.
    - Do not invent course names, durations, fees, or certifications unless they are clearly present in the catalog or context.
    - Do not rely on generic internet knowledge or broad assumptions.
    - Do not repeat promotional claims like "over 2000 courses" unless they are directly supported by the context.
    - Keep the response natural, concise, and professional.
    - Prefer a short answer with 2-4 bullets if the context contains multiple offerings.

    Previous Conversation:
    {sanitized_history}

    Brochure Catalog:
    {BROCHURE_COURSE_CATALOG}

    Institutional Context:
    {context}

    User Query:
    {query}

    If the query is unclear or not about program recommendations, reply exactly:
    "I'm sorry, I couldn't understand your request. Please rephrase or ask about programs, courses, admissions, payments, or technical support."

    Important output rule:
    - If the Institutional Context contains brochure details, summarize them directly.
    - Do not answer with broad generic marketing text when specific course information is available.
    """

    response = llm.invoke(prompt)

    return response