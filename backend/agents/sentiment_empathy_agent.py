import os

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

from rag.retriever import retrieve_documents

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "llama3")

llm = OllamaLLM(model=MODEL, base_url=OLLAMA_URL)


def sentiment_empathy_agent(query, history):

    retrieved_docs = retrieve_documents(query)

    context = "\n".join([
        doc.page_content
        for doc in retrieved_docs
    ])

    prompt = f"""
    You are the Sentiment & Empathy Agent for Technovalley.

    Your responsibilities:
    - Detect frustration or confusion
    - Respond empathetically
    - Calm users professionally
    - Provide emotionally intelligent responses
    - Maintain a supportive tone
    - Use institutional context accurately

    Previous Conversation:
    {history}

    Institutional Context:
    {context}

    User Query:
    {query}

    RESPONSE FORMAT:
    - Use clear section headings.
    - Start directly with the answer.
    - Use bullet points when helpful.
    - Do not greet the user unless they greet first.
    - Do not use the user's name unless it appears in the current message.
    - Do not use phrases such as "I'm glad", "Nice to hear from you again", or "Best regards".
    - Do not sign responses.
    - Keep answers concise and professional.
    - End with a relevant follow-up question when appropriate.

    Respond with empathy, professionalism, and support.
    """

    response = llm.invoke(prompt)

    return response