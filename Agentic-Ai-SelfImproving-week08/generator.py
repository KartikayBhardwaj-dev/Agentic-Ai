from llm import llm

# -------ANSWER GENERATOR----------
def generate_answer(question):
    prompt = f"""
Answer the question clearly and accurately
Question: {question}"""
    response = llm.invoke(prompt)
    return response.content
