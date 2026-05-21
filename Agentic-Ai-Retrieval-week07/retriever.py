from planner import rewrite_query

def generate_queries(query):

    rewritten = rewrite_query(query)

    return [
        query,
        rewritten,
        f"{query} in AI systems",
        f"{query} workflow explanation"
    ]