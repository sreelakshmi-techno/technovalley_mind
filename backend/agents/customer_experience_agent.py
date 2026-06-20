from langchain_ollama import OllamaLLM

from rag.retriever import retrieve_documents

llm = OllamaLLM(model="llama3")


def customer_experience_agent(
    query,
    history,
    session_id=None
):

    lower_query = query.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    thanks = [
        "thanks",
        "thank you",
        "ok",
        "okay"
    ]

    if lower_query in greetings:
        return (
            "Hello! Welcome to Technovalley.\n\n"
            "How can I assist you today?"
        )

    if lower_query in thanks:
        return (
            "You're welcome! Feel free to ask if you need any further assistance."
        )

    small_talk = greetings + thanks

    if lower_query in small_talk:
        context = ""
    else:
        retrieved_docs = retrieve_documents(query)
        context = "\n".join([
            doc.page_content
            for doc in retrieved_docs
        ])

    # LAST 5 MESSAGES ONLY
    formatted_history = "\n".join([
        f"User: {chat['user']}\nAssistant: {chat['assistant']}"
        for chat in history[-5:]
    ])

    if lower_query in [
        "ai",
        "artificial intelligence",
        "ai programs",
        "ai program",
        "ai courses"
    ]:
        return (
            "Artificial Intelligence Programs at Technovalley\n\n"
            "• PG Diploma in AI & Machine Learning\n"
            "• Machine Learning with Python\n"
            "• Deep Learning\n"
            "• Computer Vision\n"
            "• NLP\n"
            "• AI Internship Programs\n\n"
            "Would you like recommendations based on your background?"
        )

    if lower_query in [
        "technovalley",
        "tell me about technovalley",
        "about technovalley",
        "tell me about techvalley",
        "what is technovalley",
        "what is techvalley"
    ]:
        return (
            "Technovalley is a technology upskilling and innovation organization focused on:\n\n"
            "• Artificial Intelligence & Machine Learning\n"
            "• Data Science\n"
            "• Cybersecurity\n"
            "• Software Development\n"
            "• Emerging Technologies\n\n"
            "We provide industry-oriented training programs, internships, live projects, and career guidance to help students and professionals build practical skills."
        )

    if lower_query in [
        "what courses do you offer",
        "courses do you offer",
        "which courses do you offer",
        "what courses do you offer?",
        "which courses do you offer?"
    ]:
        return (
            "We offer programs in:\n\n"
            "• Artificial Intelligence & Machine Learning\n"
            "• Data Science\n"
            "• Cybersecurity\n"
            "• Full Stack Development\n"
            "• Cloud Computing\n"
            "• Digital Marketing\n\n"
            "Would you like recommendations based on your background or career goals?"
        )

    prompt = build_prompt(
        query=query,
        context=context,
        history=formatted_history
    )

    response = llm.invoke(prompt)

    return response


def build_prompt(
    query,
    context,
    history
):
    return f"""
    You are the Customer Experience Agent for Technovalley.

    USER CONTEXT:
    Use available user information only if it helps answer the question.
    Do not mention stored profiles unless explicitly asked.

    PREVIOUS CONVERSATION:
    {history}

    INSTITUTIONAL CONTEXT:
    {context}

    CURRENT USER MESSAGE:
    {query}

    RULES:
    - Answer the user's current question directly.
    - Speak politely and professionally at all times.
    - Focus only on Technovalley and the courses or programs it offers.
    - Do not mention other institutions, competitors, or unrelated topics.
    - Do not invent course details.
    - Do not repeat greetings.
    - Do not mention previous conversations.
    - Do not mention internal memory.
    - Do not expose user profiles.
    - Keep responses concise, natural, and professional.
    - Avoid repeating information.
    - Use short bullet points when helpful.
    - Focus on the latest user query.
    - If the query is unclear or not related to Technovalley services, reply exactly:
      "I'm sorry, I couldn't understand your request.\n\nCould you please rephrase it or let me know how I can assist you regarding Technovalley courses, admissions, internships, payments, or technical support?"

    RESPONSE STYLE:
    - Start directly with the answer.
    - Avoid introductions unless the conversation starts.
    - Keep answers focused on the user's query.
    - Use the institutional context and retrieved documents as the source of truth.
    - Prefer a short direct answer followed by 2-4 bullet points when helpful.
    - Avoid long paragraph-only replies.
    - Avoid generic marketing text if specific course details are available.
    - End with one relevant follow-up question only when it helps the user.
    - Use clear line breaks so the response is easy to scan.
    """
