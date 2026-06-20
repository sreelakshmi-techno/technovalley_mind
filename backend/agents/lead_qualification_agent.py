from langchain_ollama import OllamaLLM

from rag.retriever import retrieve_documents

llm = OllamaLLM(model="llama3")


def lead_qualification_agent(query, history):

    retrieved_docs = retrieve_documents(query)

    context = "\n".join([
        doc.page_content
        for doc in retrieved_docs
    ])

    prompt = f"""
    You are the Lead Qualification Agent for Technovalley.

    Your responsibilities:
    - Analyze student interest
    - Identify serious leads
    - Encourage conversions professionally
    - Guide users toward suitable programs
    - Maintain a professional counselling tone
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
    - Use bullet points for lead insights and next steps.
    - Do not greet the user unless they greet first.
    - Do not use the user's name unless it appears in the current message.
    - Do not use phrases such as "I'm glad", "Nice to hear from you again", or "Best regards".
    - Do not sign responses.
    - Keep answers concise and professional.
    - End with a relevant follow-up question when appropriate.

    Respond professionally and strategically.
    """

    response = llm.invoke(prompt)

    return response