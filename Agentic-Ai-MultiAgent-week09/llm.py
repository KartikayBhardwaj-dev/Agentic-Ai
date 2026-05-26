from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv
load_dotenv()

# -----------LLM CALL---------
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)
def call_llm(prompt):
    response = llm.invoke(prompt)
    return response.content