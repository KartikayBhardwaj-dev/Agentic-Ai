import redis 
import os 

# -------REDIS CLIENT INITIALIZATION-------
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    decode_responses=True
)
