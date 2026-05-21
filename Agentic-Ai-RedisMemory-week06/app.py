from dotenv import load_dotenv
load_dotenv()
from assistant import chat

print("AI personal assistant")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat(user_input)
    print(f"Assistant: {response}\n")