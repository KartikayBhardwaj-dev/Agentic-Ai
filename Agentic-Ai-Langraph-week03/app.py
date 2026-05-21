import streamlit as st
from graph import app

st.title("🔷 LangGraph Research Workflow Agent")

question = st.text_input("Enter research question")

if st.button("Run Workflow"):

    result = app.invoke({
        "question": question
    })

    st.write(result["final_answer"])