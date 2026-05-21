import time

def retry(func, retries=3):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Retry {attempt+1} failed: {e}")
            time.sleep(1)

    raise Exception("Max retries reached")