# --------RESEARCHER AGENT------
from llm import call_llm

def researcher(task):
    prompt = f"""
You are a researcher
Task:
{task}
Extract key Facts, data points, and important information"""
    return call_llm(prompt)