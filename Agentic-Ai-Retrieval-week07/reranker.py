def rerank_documents(query, docs):

    scored = []

    for doc in docs:

        score = 0

        query_words = query.lower().split()

        for word in query_words:
            if word in doc.page_content.lower():
                score += 1

        scored.append((score, doc))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [doc for score, doc in scored]