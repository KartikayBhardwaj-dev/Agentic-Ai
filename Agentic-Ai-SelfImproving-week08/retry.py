from llm import llm
import re

# -----------EXTRACT SCORE---------
def extract_score(critic):
    match = re.search(r"SCORE:\s*(\d+)", critic)

    if match:
        return int(match.group(1))
    
    return 0

# --------IMPROVE ANSWER AGENT --------
def improve_answer(question, old_answer, critic):
    prompt = f"""
    Improve this answer using critic feedback.
    Question:
    {question}
    Old Answer:
    {old_answer}
    Critic:
    {critic}
    Generate a better answer.
    """
    response = llm.invoke(prompt)
    return response.content