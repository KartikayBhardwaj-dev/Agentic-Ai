from llm import llm
from tools import search_web

# --------PLANNER NODE---------
def planner_node(state):
    prompt = f"""
You are a Research Planner.
Create A Research Plan for 
{state['question']}"""
    response = llm.invoke(prompt)
    return {
        "plan": response.content}

# -------RETRIEVER NODE--------------
def retriever_node(state):
    documents = search_web(state["question"])
    return {
        "documents": documents
    }


# ------SUMMARIZER NODE------------
def summarize_node(state):
    prompt = f"""
Research Plan: {state['plan']}
Documents: {state['documents']}
Generate a Clean summary
"""
    response = llm.invoke(prompt)
    return {
        "summary": response.content
    }

# -------CRITIC NODE------------
def critic_node(state):

    prompt = f"""

    Critique this summary:

    {state['summary']}

    Check:

    - correctness

    - completeness

    - clarity

    If good:

    APPROVED

    Otherwise:

    REVISE

    """

    response = llm.invoke(prompt)

    critique = response.content

    if "APPROVED" in critique:

        return {

            "critique": "APPROVED",

            "final_answer": state["summary"]

        }

    return {

        "critique": critique

    }