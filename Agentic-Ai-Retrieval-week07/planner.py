from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

def rewrite_query(query):
    prompt = f"""
Rewrite this query for better document retrieval
Query: {query}"""

    response = llm.invoke(prompt)

    return response.content