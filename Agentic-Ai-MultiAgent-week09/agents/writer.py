# agents/writer.py
from llm import call_llm

def writer(text: str):
    prompt = f"""
    You are a professional writer.

    Convert this into a clean final report:

    {text}
    """
    return call_llm(prompt)