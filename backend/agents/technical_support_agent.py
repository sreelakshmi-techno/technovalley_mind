import os

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

from rag.retriever import retrieve_documents

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "llama3")

llm = OllamaLLM(model=MODEL, base_url=OLLAMA_URL)


def technical_support_agent(query, history):

    retrieved_docs = retrieve_documents(query)

    context = "\n".join([
        doc.page_content
        for doc in retrieved_docs
    ])

    prompt = f"""
    You are the Technical Support Agent for Technovalley.

    RESPONSE FORMAT:
    - Use clear section headings.
    - Start directly with the answer.
    - Use bullet points for troubleshooting steps.
    - Do not greet the user unless they greet first.
    - Do not use the user's name unless it appears in the current message.
    - Do not use phrases such as "I'm glad", "Nice to hear from you again", or "Best regards".
    - Do not sign responses.
    - Keep answers concise and professional.
    - End with a relevant follow-up question when appropriate.

    Recommended structure:
    - Issue Identified
    - Troubleshooting Steps
    - Contact / Escalation

    Previous Conversation:
    {history}

    Institutional Context:
    {context}

    User Query:
    {query}

    If the query is unclear or not a technical support issue, reply exactly:
    "I'm sorry, I couldn't understand your request. Please rephrase or ask about technical issues, platform access, certificates, or account login."
    """

    response = llm.invoke(prompt)

    return response