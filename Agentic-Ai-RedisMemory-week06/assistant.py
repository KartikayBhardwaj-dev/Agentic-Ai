from langchain_groq import ChatGroq
from memory import save_memory, get_memories
import os

# -----LLM---------
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# -----CHAT---------
def chat(user_input):
    memories = get_memories()
    memory_context = "\n".join(memories)
    prompt = f"""
You are helpful Ai Assistant
Previous Memories: {memory_context}
User: {user_input}"""
    response = llm.invoke(prompt)
    answer = response.content
    save_memory(f"USER: {user_input}")
    save_memory(f"ASSISTANT: {answer}")
    return answer