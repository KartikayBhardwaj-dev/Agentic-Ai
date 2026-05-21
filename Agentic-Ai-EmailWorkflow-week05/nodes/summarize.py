from langchain_groq import ChatGroq
from utils.logger import log_step
import os 
# -------LLM CALL-------
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# ---------SUMMARIZE AGENT------------
def summarize_node(state):
    email = state["email"]
    prompt = f"""
Summarize this email clearly:
{email}"""
    response = llm.invoke(prompt)
    summary = response.content
    log_step("summary", summary)

    return {
    "summary": summary
}