from dotenv import load_dotenv
load_dotenv()

from vector_store import build_vectorstore
from retriever import generate_queries
from reranker import rerank_documents
from compressor import compress_context

from langchain_groq import ChatGroq
import os

vectordb = build_vectorstore()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

query = input("Ask Question: ")

queries = generate_queries(query)

all_docs = []

for q in queries:

    docs = vectordb.similarity_search(q, k=2)

    all_docs.extend(docs)

reranked_docs = rerank_documents(query, all_docs)

compressed_context = compress_context(reranked_docs[:3])

prompt = f"""
Answer the question using context below.

Context:
{compressed_context}

Question:
{query}
"""

response = llm.invoke(prompt)

print("\nANSWER:\n")
print(response.content)