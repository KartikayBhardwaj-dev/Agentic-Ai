from llm import call_llm

def critic(text):
    prompt = f"""
You are a critic
Review this content and check:
-factual issues
-logic error
-missing points
Content:
{text}
Return improvements."""
    return call_llm(prompt)