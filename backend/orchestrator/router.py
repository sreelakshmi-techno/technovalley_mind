from orchestrator.intent_classifier import classify_intent


def router(state):

    query = state["query"].strip()
    lowered_query = query.lower().strip()
    conversation_state = state.get("conversation_state", {})

    intent = classify_intent(query)

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if intent == "GREETING" or lowered_query in greetings:
        return "customer_experience"

    # Keep state lightweight; do not force the next turn into a form-filling path.

    # PROGRAM RECOMMENDATION AGENT FOR AI-RELATED QUERIES
    if intent == "COURSE_QUERY" or any(word in lowered_query for word in [
        "ai",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "computer vision",
        "nlp"
    ]):
        return "program_recommendation"

    # FAQ AGENT
    if intent == "GENERAL" and any(word in lowered_query for word in [
        "timing",
        "certificate",
        "location",
        "branch",
        "contact"
    ]):
        return "faq"


    # PAYMENT & ENROLLMENT AGENT
    elif intent == "PAYMENT" or any(word in lowered_query for word in [
        "payment",
        "fees",
        "fee",
        "emi",
        "installment",
        "enrollment",
        "pay"
    ]):
        return "payment_enrollment"


    # COUNSELLING & ADMISSION AGENT
    elif intent == "ADMISSION" or any(word in lowered_query for word in [
        "admission",
        "apply",
        "eligibility",
        "join",
        "enroll"
    ]):
        return "counselling_admission"


    # TECHNICAL SUPPORT AGENT
    elif intent == "SUPPORT" or any(word in lowered_query for word in [
        "login",
        "password",
        "technical",
        "issue",
        "problem",
        "certificate download",
        "lms",
        "portal",
        "support",
        "access"
    ]):
        return "technical_support"


    # HR & TALENT AGENT
    elif any(word in lowered_query for word in [
        "placement",
        "placements",
        "internship",
        "internships",
        "career",
        "recruitment",
        "job",
        "hiring",
        "hr"
    ]):
        return "hr_talent"


    # LEAD QUALIFICATION AGENT
    elif any(word in lowered_query for word in [
        "interested",
        "looking for",
        "career change",
        "future",
        "best course",
        "which course",
        "confused",
        "guidance"
    ]):
        return "lead_qualification"


    # PROGRAM RECOMMENDATION AGENT
    elif any(word in lowered_query for word in [
        "recommend",
        "suggest",
        "course",
        "program"
    ]):
        return "program_recommendation"


    # SENTIMENT & EMPATHY AGENT
    elif any(word in lowered_query for word in [
        "frustrated",
        "angry",
        "upset",
        "disappointed",
        "not working",
        "bad experience",
        "unhappy"
    ]):
        return "sentiment_empathy"


    # MARKETING & NURTURE AGENT
    elif any(word in lowered_query for word in [
        "webinar",
        "workshop",
        "event",
        "promotion",
        "offer",
        "demo class",
        "training session",
        "awareness"
    ]):
        return "marketing_nurture"


    # WORKFLOW COORDINATION AGENT
    elif any(word in lowered_query for word in [
        "workflow",
        "complete process",
        "full process",
        "step by step",
        "course and payment",
        "admission and fees"
    ]):
        return "workflow_coordination"


    # DEFAULT CUSTOMER EXPERIENCE
    return "customer_experience"