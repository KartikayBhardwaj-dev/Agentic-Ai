from dotenv import load_dotenv
load_dotenv()

from graph import graph

email = """
URGENT:
Production server is down.
Customers cannot access the application.
Need immediate response.
"""

result = graph.invoke({
    "email": email
})

print("\nFINAL RESULT\n")
print(result)