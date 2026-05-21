from langgraph.graph import StateGraph, END
from state import WorkflowState
from nodes.notify import notify_node
from nodes.prioritize import prioritize_node
from nodes.report import report_node
from nodes.summarize import summarize_node

# ---------WORKFLOW----------
workflow = StateGraph(WorkflowState)

# -----------ADD NODES IN GRAPH---------
workflow.add_node("summarize", summarize_node)
workflow.add_node("prioritize", prioritize_node)
workflow.add_node("notify", notify_node)
workflow.add_node("report", report_node)

# -------ADD ENTRY POINT OF GRAPH--------
workflow.set_entry_point("summarize")

# --------ADD EDGES BETWEEN NODES ---------
workflow.add_edge("summarize", "prioritize")

# -----------CONDITIONAL BRANCHING-----------
def route_priority(state):
    if "HIGH" in state["priority"]:
        return "notify"
    return "report"

workflow.add_conditional_edges(
    "prioritize",
    route_priority,
    {
        "notify": "notify",
        "report": "report"
    }
)

# -------ADD EDGE BET NODES------
workflow.add_edge("notify", "report")
workflow.add_edge("report", END)
graph = workflow.compile()

