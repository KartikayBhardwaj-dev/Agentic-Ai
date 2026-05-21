import streamlit as st
from assistant import MemoryAssistant

assistant = MemoryAssistant()

st.title("🧠 Persistent AI Assistant")

user_input = st.text_input(
    "Talk with the assistant"
)

if st.button("Send"):

    response = assistant.chat(user_input)

    st.write(response)