from redis_store import redis_client
MEMORY_KEY = "user_memory"

def save_memory(memory):
    redis_client.rpush(MEMORY_KEY, memory)

def get_memories():
    return redis_client.lrange(MEMORY_KEY, 0, -1)