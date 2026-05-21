from langchain.tools import tool

@tool
def calculator_tool(expression: str) -> str:
    """
    Perform mathematical calculations.
    Input should be a valid math expression.
    """

    try:

        result = eval(expression)

        return f"Result: {result}"

    except Exception as e:

        return f"Calculation error: {str(e)}"