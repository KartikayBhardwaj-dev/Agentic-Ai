from utils.logger import log_step

def notify_node(state):
    log_step(
        "NOTIFICATION",
        "High priority email detected!"
    )

    return {}