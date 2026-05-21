from tavily import TavilyClient
import os 
from dotenv import load_dotenv
load_dotenv()

# ----------CLIENT CALLING---------
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# -----------SEARCH TOOL----------
def search_web(query: str):
    response = client.search(query=query, search_depth="basic")

    results = []
    for r in response.get("results", []):
        results.append({
            "title": r.get("title"),
            "url": r.get("url"),
            "content": r.get("content")
        })

        return results