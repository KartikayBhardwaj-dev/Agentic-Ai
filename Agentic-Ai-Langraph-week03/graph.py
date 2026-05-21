from langgraph.graph import StateGraph, END
from state import GraphState
from nodes import (planner_node, retriever_node, summarize_node, critic_node)

# ------------WORKFLOW / COMBINE ALL NODES----------
workflow = StateGraph(GraphState)

workflow.add_node("planner", planner_node)
workflow.add_node("retriever", retriever_node)
workflow.add_node("summarizer", summarize_node)
workflow.add_node("critic", critic_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "retriever")
workflow.add_edge("retriever", "summarizer")
workflow.add_edge("summarizer", "critic")

# -----CONDITIONAL ROUTING FROM CRITIC --------
def route_decision(state):
    if state["critique"] == "APPROVED":
        return END
    return "retriever"
workflow.add_conditional_edges(

    "critic",

    route_decision

)

app = workflow.compile()
