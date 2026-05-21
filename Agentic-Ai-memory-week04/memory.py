import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./vector_store")

collection = client.get_or_create_collection(

    name="chat_memory"

)

embedding_model = SentenceTransformer(

    "all-MiniLM-L6-v2"

)

def store_memory(text, memory_id):
    embedding = embedding_model.encode(text).tolist()
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[memory_id]
    )

def retrieve_memory(query, top_k=3):

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]