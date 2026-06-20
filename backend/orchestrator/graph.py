from langgraph.graph import StateGraph, END

from orchestrator.state import AgentState
from orchestrator.router import router

from agents.customer_experience_agent import (
    customer_experience_agent
)

from agents.faq_agent import faq_agent

from agents.program_recommendation_agent import (
    program_recommendation_agent,
    sanitize_history
)

from agents.counselling_admission_agent import (
    counselling_admission_agent
)

from agents.payment_enrollment_agent import (
    payment_enrollment_agent
)

from agents.hr_talent_agent import (
    hr_talent_agent
)

from agents.technical_support_agent import (
    technical_support_agent
)

from agents.lead_qualification_agent import (
    lead_qualification_agent
)

from agents.sentiment_empathy_agent import (
    sentiment_empathy_agent
)

from agents.marketing_nurture_agent import (
    marketing_nurture_agent
)

from agents.workflow_coordination_agent import (
    workflow_coordination_agent
)

from memory.memory_manager import (
    get_memory,
    save_memory
)

from memory.short_memory import (
    conversation_store
)

from memory.state_manager import (
    get_conversation_state,
    update_conversation_state
)


# CUSTOMER EXPERIENCE NODE
def customer_node(state):
    print("CUSTOMER EXPERIENCE AGENT CALLED")

    session_id = state["session_id"]

    try:

        memory = get_memory(session_id)

        history = sanitize_history(memory.get("short_memory", []))

    except Exception as e:

        print(
            "Memory retrieval error:",
            e
        )

        history = []


    response = customer_experience_agent(

        state["query"],

        history,

        session_id

    )


    try:

        save_memory(

            session_id,

            state["query"],

            response

        )

    except Exception as e:

        print(
            "Memory save error:",
            e
        )


    return {
        "response": response
    }


# FAQ NODE
def faq_node(state):
    print("FAQ AGENT CALLED")

    response = faq_agent(
        state["query"]
    )

    return {
        "response": response
    }


# PROGRAM RECOMMENDATION NODE
def recommendation_node(state):
    print("PROGRAM RECOMMENDATION AGENT CALLED")

    session_id = state["session_id"]
    conversation_state = get_conversation_state(session_id)

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    agent_query = state["query"]

    response = program_recommendation_agent(
        agent_query,
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# COUNSELLING & ADMISSION NODE
def counselling_node(state):
    print("COUNSELLING & ADMISSION AGENT CALLED")

    session_id = state["session_id"]

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    response = counselling_admission_agent(
        state["query"],
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# PAYMENT & ENROLLMENT NODE
def payment_node(state):
    print("PAYMENT & ENROLLMENT AGENT CALLED")

    session_id = state["session_id"]

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    response = payment_enrollment_agent(
        state["query"],
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# HR & TALENT NODE
def hr_node(state):
    print("HR & TALENT AGENT CALLED")

    session_id = state["session_id"]

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    response = hr_talent_agent(
        state["query"],
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# TECHNICAL SUPPORT NODE
def technical_node(state):
    print("TECHNICAL SUPPORT AGENT CALLED")

    session_id = state["session_id"]

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    response = technical_support_agent(
        state["query"],
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# LEAD QUALIFICATION NODE
def lead_node(state):
    print("LEAD QUALIFICATION AGENT CALLED")

    session_id = state["session_id"]

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    response = lead_qualification_agent(
        state["query"],
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# SENTIMENT & EMPATHY NODE
def sentiment_node(state):
    print("SENTIMENT & EMPATHY AGENT CALLED")

    session_id = state["session_id"]

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    response = sentiment_empathy_agent(
        state["query"],
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# MARKETING & NURTURE NODE
def marketing_node(state):
    print("MARKETING & NURTURE AGENT CALLED")

    session_id = state["session_id"]

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    response = marketing_nurture_agent(
        state["query"],
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# WORKFLOW COORDINATION NODE
def workflow_node(state):
    print("WORKFLOW COORDINATION AGENT CALLED")

    session_id = state["session_id"]

    history = sanitize_history(
        conversation_store.get(
            session_id,
            []
        )
    )

    response = workflow_coordination_agent(
        state["query"],
        history
    )

    history.append({
        "user": state["query"],
        "assistant": response
    })

    conversation_store[session_id] = history

    return {
        "response": response
    }


# CREATE WORKFLOW
workflow = StateGraph(AgentState)


# REGISTER NODES
workflow.add_node(
    "customer_experience",
    customer_node
)

workflow.add_node(
    "faq",
    faq_node
)

workflow.add_node(
    "program_recommendation",
    recommendation_node
)

workflow.add_node(
    "counselling_admission",
    counselling_node
)

workflow.add_node(
    "payment_enrollment",
    payment_node
)

workflow.add_node(
    "hr_talent",
    hr_node
)

workflow.add_node(
    "technical_support",
    technical_node
)

workflow.add_node(
    "lead_qualification",
    lead_node
)

workflow.add_node(
    "sentiment_empathy",
    sentiment_node
)

workflow.add_node(
    "marketing_nurture",
    marketing_node
)

workflow.add_node(
    "workflow_coordination",
    workflow_node
)


# ROUTER ENTRY
workflow.set_conditional_entry_point(
    router
)


# EDGES
workflow.add_edge(
    "customer_experience",
    END
)

workflow.add_edge(
    "faq",
    END
)

workflow.add_edge(
    "program_recommendation",
    END
)

workflow.add_edge(
    "counselling_admission",
    END
)

workflow.add_edge(
    "payment_enrollment",
    END
)

workflow.add_edge(
    "hr_talent",
    END
)

workflow.add_edge(
    "technical_support",
    END
)

workflow.add_edge(
    "lead_qualification",
    END
)

workflow.add_edge(
    "sentiment_empathy",
    END
)

workflow.add_edge(
    "marketing_nurture",
    END
)

workflow.add_edge(
    "workflow_coordination",
    END
)


# COMPILE GRAPH
graph = workflow.compile()