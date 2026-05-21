from langchain_groq import ChatGroq
from utils.logger import log_step
import os 

# ---------LLM CALL---------
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# ---------PRIORITY CLASSIFICATION AGENT-------
def prioritize_node(state):
    summary = state["summary"]

    prompt = f"""
Classify this email priority:
HIGH OR LOW
Email: 
{summary}
"""
    response = llm.invoke(prompt)
    priority = response.content.strip().upper()
    log_step("priority", priority)

    return {
        "priority": priority
    }