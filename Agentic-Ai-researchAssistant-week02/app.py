import streamlit as st
from agent import ReActAgent

st.set_page_config(page_title="ReAct Research Agent")

st.title("🔍 ReAct Research Assistant (Groq + LangChain)")

question = st.text_input("Ask a research question:")

if st.button("Run Agent"):
    agent = ReActAgent()
    result = agent.run(question)

    st.markdown("## 📌 Final Output")
    st.write(result)