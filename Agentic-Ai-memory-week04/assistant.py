from llm import llm
from memory import (
    store_memory,
    retrieve_memory
)

class MemoryAssistant:

    def chat(self, user_input):

        memories = retrieve_memory(user_input)

        prompt = f"""
        Relevant Memories:
        {memories}

        User Message:
        {user_input}

        Respond helpfully while using memory context.
        """

        response = llm.invoke(prompt)

        store_memory(
            user_input,
            f"user_{hash(user_input)}"
        )

        store_memory(
            response.content,
            f"assistant_{hash(response.content)}"
        )

        return response.content