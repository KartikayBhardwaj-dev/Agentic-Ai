from langchain_core.messages import (HumanMessage, SystemMessage)
from agents.llm import llm
from prompts.agent_prompt import (SYSTEM_PROMPT)
from tools.tool_registry import (TOOLS)

# ---------BIND TOOLS-------
llm_with_tools = llm.bind_tools(TOOLS)


# ------AGENT-------
def run_agent(user_query):
    print("\n==========USER QUESTION==========")
    print(user_query)

    # -------CREATE MESSAGES---------
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_query)
    ]

    # --------LLM RESPONSES-------------
    response = llm_with_tools.invoke(messages)
    # ----------SHOW RAW RESPONSES--------
    print("\n========== RAW LLM RESPONSE ==========\n")
    print(response)

    # TOOL CALL DETECTION-------
    if response.tool_calls:
        print("\n==========TOOL CALL DETECTED=========")
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print(f"Tool Name: {tool_name}")
            print(f"Tool Args: {tool_args}")
            # ---------- FIND TOOL ----------

            selected_tool = next(

                tool for tool in TOOLS

                if tool.name == tool_name

            )

            # ---------- EXECUTE TOOL ----------

            tool_result = selected_tool.invoke(

                tool_args

            )

            print("\n========== TOOL RESULT ==========\n")

            print(tool_result)

            # ---------- FINAL RESPONSE ----------

            final_messages = [

                SystemMessage(

                    content=SYSTEM_PROMPT

                ),

                HumanMessage(

                    content=user_query

                ),

                response,

                {

                    "role": "tool",

                    "tool_call_id":

                    tool_call["id"],

                    "content": str(tool_result)

                }

            ]

            final_response = llm_with_tools.invoke(

                final_messages

            )

            print("\n========== FINAL ANSWER ==========\n")

            print(final_response.content)

            return final_response.content

    # ---------- DIRECT RESPONSE ----------

    print("\n========== FINAL ANSWER ==========\n")

    print(response.content)

    return response.content