RESTRICTED_TOPICS = [
    "competitor",
    "better institute",
    "other institute",
    "compare institute",
    "weakness of technovalley",
    "bad review"
]


def policy_agent(query):

    lower_query = query.lower()

    for topic in RESTRICTED_TOPICS:

        if topic in lower_query:

            return {
                "blocked": True,
                "response": (
                    "I can help you with information about "
                    "Technovalley’s programs, services, "
                    "career guidance, and support systems."
                )
            }

    return {
        "blocked": False
    }