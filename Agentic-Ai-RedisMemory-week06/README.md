# 🧠 AI Personal Assistant — Long-Term Memory System

A memory-enabled AI assistant built using:

- Redis
- LangChain
- Groq LLM
- Persistent memory architecture

This project demonstrates how production AI systems store, retrieve, and use long-term memory across conversations.

---

# 🚀 Overview

The assistant can:

- remember previous conversations
- store user preferences
- recall tasks and information
- persist memory across sessions
- retrieve memory for contextual responses

Unlike basic chatbots, this system maintains persistent conversational memory.

---

# 🏗 Memory Architecture

```text
User Input
    ↓
Memory Retrieval
    ↓
Redis Memory Store
    ↓
Context Injection
    ↓
LLM Response
    ↓
Memory Persistence
```

---

# 🧠 Memory Flow

```text
User: I like Python

        ↓

Store in Redis

        ↓

Retrieve Later

        ↓

Inject Into Prompt

        ↓

AI Responds With Memory
```

---

# 🧩 Types of Memory Covered

| Memory Type | Description |
|---|---|
| Short-Term Memory | Current conversation context |
| Long-Term Memory | Persistent stored information |
| Semantic Memory | Facts/preferences about user |
| Episodic Memory | Past interaction history |
| Vector Memory | Embedding-based retrieval concepts |

---

# ⚙️ Features

- persistent Redis memory
- conversational memory
- preference recall
- task remembrance
- retrieval-based context injection
- session persistence
- modular memory architecture

---

# 📁 Project Structure

```text
ai_memory_assistant/
│
├── app.py
├── assistant.py
├── memory.py
├── redis_store.py
├── requirements.txt
└── .env
```

---

# 🧠 Retrieval Pipeline

```text
User Query
    ↓
Fetch Stored Memories
    ↓
Build Context
    ↓
Inject Into Prompt
    ↓
Generate Personalized Response
```

---

# 🛠 Tech Stack

| Layer | Technology |
|---|---|
| LLM | Groq |
| Framework | LangChain |
| Memory Store | Redis |
| Backend Language | Python |

---

# ▶ Run Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Redis

```bash
brew services start redis
```

---

## Run Assistant

```bash
python app.py
```

---

# 🧪 Example

## Input

```text
I like FastAPI backend development
```

Later:

```text
What do I like?
```

---

## Output

```text
You like FastAPI backend development.
```

---

# 🧠 Key Learnings

- long-term AI memory systems
- Redis-based persistence
- retrieval pipelines
- conversational memory
- memory injection into prompts
- stateful AI assistant architecture
- production memory concepts

---

# ✅ Outcome

This project transforms a basic chatbot into a memory-enabled AI assistant capable of persistent contextual interactions across sessions.