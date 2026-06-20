from langchain_ollama import OllamaLLM

from rag.retriever import retrieve_documents

llm = OllamaLLM(model="llama3")


def counselling_admission_agent(query, history):
    lower_query = query.lower().strip()

    if lower_query in [
        "admission process",
        "admission process?",
        "how to apply",
        "how do i apply",
        "how do i enroll",
        "admissions",
        "admission"
    ]:
        return (
            "Admission Process at Technovalley\n\n"
            "1. Submit your enquiry or application.\n"
            "2. Speak with our counselling team.\n"
            "3. Choose the appropriate program.\n"
            "4. Complete the registration process.\n"
            "5. Pay the applicable fees.\n"
            "6. Receive confirmation and onboarding details.\n\n"
            "If you'd like assistance with a specific course admission, please let me know."
        )

    retrieved_docs = retrieve_documents(query)

    context = "\n".join([
        doc.page_content
        for doc in retrieved_docs
    ])

    prompt = f"""
    You are the Counselling & Admission Agent for Technovalley.

    RESPONSE FORMAT:
    - Use clear section headings.
    - Use bullet points or numbered steps.
    - Start directly with the answer.
    - Do not greet the user unless they greet first.
    - Do not use the user's name unless it appears in the current message.
    - Do not use phrases such as "I'm glad", "Nice to hear from you again", or "Best regards".
    - Do not sign responses.
    - Keep answers concise and professional.
    - End with a relevant follow-up question when appropriate.

    Recommended structure:
    - Title
    - Process Steps
    - Requirements
    - Next Step

    Previous Conversation:
    {history}

    Institutional Context:
    {context}

    User Query:
    {query}

    If the query is unclear or unrelated to admission, reply exactly:
    "I'm sorry, I couldn't understand your request. Could you please rephrase it or let me know how I can assist you regarding admissions, programs, enrollment, or payment?"
    """

    response = llm.invoke(prompt)

    return response