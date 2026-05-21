from utils.logger import log_step

def report_node(state):
    report = f"""
    EMAIL REPORT

    Summary:
    {state['summary']}

    Priority:
    {state['priority']}
    """

    log_step("report", report)

    return {
        "report": report
    }