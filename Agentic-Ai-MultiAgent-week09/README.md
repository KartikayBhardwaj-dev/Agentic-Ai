# 🔸 WEEK 9 — Multi-Agent Fundamentals  
## 🛠 Mini Project: Multi-Agent Research Team

This project demonstrates the fundamentals of multi-agent systems by building a simple collaborative AI pipeline where multiple specialized agents work together to produce a final structured output.

---

## 🧠 Objective

To understand how multi-agent systems work using:
- Supervisor-based control flow  
- Task delegation between agents  
- Shared memory/state passing  
- Sequential coordination of agents  

---

## 🤖 System Flow

User Query → Supervisor Agent → Researcher Agent → Summarizer Agent → Critic Agent → Writer Agent → Final Output

---

## 🧩 Agents Overview

**📚 Researcher Agent**  
Collects raw information and generates initial research content.

**📝 Summarizer Agent**  
Converts raw research into a structured and concise summary.

**⚖️ Critic Agent**  
Reviews the output for clarity, correctness, and logical consistency.

**✍️ Writer Agent**  
Produces the final polished and readable report.

---

## 🧠 Supervisor Role

The supervisor manages the workflow by:
- Controlling execution order  
- Passing data between agents  
- Maintaining shared state  
- Ensuring smooth pipeline execution  

---

## 🔄 Shared Memory (State)

All agents operate on a shared state object:

```python
state = {
    "query": "",
    "research": "",
    "summary": "",
    "critique": "",
    "final_report": ""
}