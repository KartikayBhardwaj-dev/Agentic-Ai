from typing import List, TypedDict

class GraphState(TypedDict):
    question: str
    plan: str
    documents: List[str]
    summary: str
    critique: str
    final_answer: str
    