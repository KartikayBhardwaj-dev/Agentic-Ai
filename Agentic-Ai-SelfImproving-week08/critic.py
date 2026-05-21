from llm import llm

# --------CRITIC AGENT-------
def critic_answer(question, answer):
    prompt = f"""

    Evaluate this answer.

    Question:

    {question}

    Answer:

    {answer}

    Check:

    - correctness

    - clarity

    - completeness

    Give:

    - critique

    - score out of 10

    Format:

    SCORE: number

    CRITIC: feedback

    """

    response = llm.invoke(prompt)
    return response.content