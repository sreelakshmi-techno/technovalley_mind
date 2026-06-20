from agents.program_recommendation_agent import (
    program_recommendation_agent
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


def workflow_coordination_agent(query, history):

    responses = []


    # COURSE + PAYMENT WORKFLOW
    if (
        "course" in query.lower()
        and
        ("payment" in query.lower() or "fees" in query.lower())
    ):

        recommendation = program_recommendation_agent(
            query,
            history
        )

        payment = payment_enrollment_agent(
            query,
            history
        )

        responses.append(
            "PROGRAM GUIDANCE:\n" + recommendation
        )

        responses.append(
            "PAYMENT GUIDANCE:\n" + payment
        )


    # COURSE + ADMISSION WORKFLOW
    elif (
        "course" in query.lower()
        and
        ("admission" in query.lower() or "apply" in query.lower())
    ):

        recommendation = program_recommendation_agent(
            query,
            history
        )

        admission = counselling_admission_agent(
            query,
            history
        )

        responses.append(
            "PROGRAM GUIDANCE:\n" + recommendation
        )

        responses.append(
            "ADMISSION GUIDANCE:\n" + admission
        )


    # PLACEMENT WORKFLOW
    elif (
        "placement" in query.lower()
        or
        "internship" in query.lower()
    ):

        hr_response = hr_talent_agent(
            query,
            history
        )

        responses.append(
            "PLACEMENT SUPPORT:\n" + hr_response
        )


    # TECHNICAL WORKFLOW
    elif (
        "login" in query.lower()
        or
        "lms" in query.lower()
    ):

        technical = technical_support_agent(
            query,
            history
        )

        responses.append(
            "TECHNICAL SUPPORT:\n" + technical
        )


    else:

        responses.append(
            "Workflow coordination completed."
        )


    final_response = "\n\n".join(responses)

    return final_response