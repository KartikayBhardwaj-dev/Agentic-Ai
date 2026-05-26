from llm import call_llm

def summarizer(text):
    prompt = f"""
You are a summarizer.
Condense this into clear structured bullet points:
{text}"""
    return call_llm(prompt)