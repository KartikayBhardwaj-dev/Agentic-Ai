from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# -------INIT EMBEDDING MODEL--------
embedding = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# -------BUILDING VECTORSTORE IN CHROMADB------
def build_vectorstore():
    with open("/Users/kartikaybhardwaj/Desktop/Agentic-Ai/Agentic-Ai-Retrieval-week07/documents/ai_notes.txt", "r") as f:
        text = f.read()

        splitter = CharacterTextSplitter(
            chunk_size=200,
            chunk_overlap=20
        )

        docs = splitter.create_documents([text])

        vectordb = Chroma.from_documents(
            docs,
            embedding=embedding,
            persist_directory="./chroma_db"
        )

        return vectordb
