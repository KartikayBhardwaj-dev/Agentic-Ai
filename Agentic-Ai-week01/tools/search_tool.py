from langchain.tools import tool

@tool
def search_tool(query: str) -> str:
    """
    Search general information.
    """

    fake_results = {

        "langchain":
        "LangChain is a framework for building LLM applications.",

        "python":
        "Python is a programming language.",

        "agent":
        "AI agents can reason and use tools."
    }

    for key, value in fake_results.items():

        if key in query.lower():

            return value

    return "No search results found."