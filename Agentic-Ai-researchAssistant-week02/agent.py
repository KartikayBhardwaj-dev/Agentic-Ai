from config import llm
from tools import search_web
class ReActAgent:
    def __init__(self):
        self.memory = []

    def think(self, question: str):
        prompt = f"""

You are a ReAct (Reason + Act + Observe) agent.

Follow this strict format:

Thought: what you should do

Action: search_web[query] OR None

Observation: result from tool (if any)

When enough information is collected:

Final Answer: structured response

Rules:

- Always reason step by step internally

- Use search_web when needed

- Do not hallucinate facts

Question: {question}

Previous Steps:

{self.memory}

"""
        response = llm.invoke(prompt)
        return response.content
    def act(self, text: str):
        if "search_web" in text:
            try:
                query = text.split("[")[1].split("]")[0]
                return search_web(query)
            except:
                return "Invalid search query format"
        return None
    def run(self, question: str):

        self.memory = []

        for _ in range(5):

            output = self.think(question)

            self.memory.append(output)

            if "Final Answer" in output:

                return output

            if "search_web" in output:

                observation = self.act(output)

                self.memory.append(f"Observation: {observation}")

        return "Failed to complete reasoning within limits"