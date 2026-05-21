# 🔍 ReAct Research Assistant (Groq + LangChain)

An autonomous AI research agent built using the ReAct (Reason + Act + Observe) framework. It can search the web, reason step-by-step, and generate structured answers using real-time information.

Powered by Groq LLM (Llama3/Mixtral), LangChain, Tavily Search API, and Streamlit UI.

---

# 🚀 Features

- ReAct reasoning loop (Thought → Action → Observation → Repeat)
- Real-time web search using Tavily API
- Multi-step reasoning instead of single-shot answers
- Iterative refinement of answers
- Scratchpad memory for tracking reasoning steps
- Autonomous decision-making (decides when to search)
- Simple Streamlit UI
- Fast inference using Groq models

---

# 🧠 Core Concepts Used

## ReAct Architecture
The agent follows a reasoning loop:

Thought → Action → Observation → Repeat → Final Answer

Instead of answering directly, the model thinks, takes actions using tools, observes results, and refines its reasoning.

---

## Iterative Reasoning
The agent improves its answer step-by-step by:
- Identifying missing information
- Searching the web when needed
- Refining reasoning across multiple cycles

---

## Tool Use (Function Calling)
The LLM dynamically decides:
- When to search
- What query to use
- How to use retrieved results

Tool used: Tavily Web Search API

---

## Scratchpad Memory
The agent stores intermediate steps:
- Thoughts
- Actions
- Observations

This helps maintain context across reasoning loops.

---

## LLM Orchestration (Groq + LangChain)
The system uses:
- ChatGroq (Llama3 / Mixtral)
- LangChain abstraction layer
- Structured prompts for controlled agent behavior

---

## Autonomous Agent Behavior
The system behaves like a simple autonomous agent that:
- Plans next steps
- Uses tools dynamically
- Stops when a final answer is reached

---

# ⚙️ Tech Stack

Groq LLM, LangChain, Tavily API, Python, Streamlit, python-dotenv

---

# 🏗️ Architecture

User Question → ReAct Agent (Groq LLM) → Thought → Action (Search Tool) → Observation → Loop → Final Answer

---

# 📁 Project Structure

react-research-assistant/
├── app.py (Streamlit UI)
├── agent.py (ReAct logic + loop)
├── tools.py (Tavily web search)
├── config_llm.py (Groq LLM setup)
├── .env (API keys)
├── requirements.txt
└── README.md

---

# ⚙️ How It Works

1. User asks a question  
2. LLM generates reasoning (Thought)  
3. If needed, it calls search tool (Action)  
4. Receives results (Observation)  
5. Repeats reasoning loop  
6. Produces final structured answer  

---

# 🔥 Example Flow

User: What is the EU AI Act?

Agent:
- Thought: Need definition and latest updates  
- Action: search_web("EU AI Act summary")  
- Observation: retrieves articles  
- Thought: need enforcement timeline  
- Action: search_web("EU AI Act enforcement timeline")  
- Final Answer: structured explanation

---

# 🧩 Why This Project Matters

This project demonstrates how modern AI systems evolve from simple chatbots into agentic systems.

It teaches:
- How reasoning loops work in LLMs
- How tools extend model capability
- How autonomous agents are built
- How real AI research assistants operate

---

# 🚀 Future Improvements

- LangGraph state-based agent design
- Multi-tool routing (calculator, file reader, APIs)
- Long-term memory using vector databases
- Self-reflection / critique loops
- Streaming responses
- Multi-agent collaboration systems

---

# 🧠 Summary

This project turns a standard LLM into a ReAct-based autonomous research agent that can think, act, and improve its answers using external tools.