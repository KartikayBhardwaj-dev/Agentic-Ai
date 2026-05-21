def compress_context(docs):

    compressed = []

    for doc in docs:
        compressed.append(doc.page_content[:150])

    return "\n".join(compressed)