import os 
from dotenv import load_dotenv
# -------------LOAD ENV VARIABLES----------
load_dotenv()

# ------API KEYS---------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---------MODEL CONFIG---------
MODEL_NAME = ("llama-3.1-8b-instant")

TEMPERATURE = 0
MAX_TOKENS = 1024
