# --------SUPERVISOR AGENT (BRAIN)--------
from agents.researcher import researcher
from agents.summarizer import summarizer
from agents.critic import critic
from agents.writer import writer

# --------SUPERVISOR DEF------
def supervisor(task):
    print("Researching..")
    research = researcher(task)

    print("Summarizing..")
    summary = summarizer(researcher)

    print("Critic Reviewing...")
    review = critic(summary)

    print("Writing final Report..")
    final_report = writer(review)

    return {
        "research": research,
        "summary": summary,
        "review": review,
        "final_write": final_report
    }