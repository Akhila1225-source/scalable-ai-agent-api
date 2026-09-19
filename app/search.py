import json


def search_tools(query, top_k=5):
    with open("data/api_catalog.json", "r") as file:
        tools = json.load(file)

    query_words = query.lower().split()
    results = []

    for tool in tools:
        score = 0

        searchable_text = (
            tool["name"] + " " +
            tool["category"] + " " +
            tool["description"] + " " +
            tool["endpoint"]
        ).lower()

        for word in query_words:
            if word in tool["name"].lower():
                score += 4

            if word in tool["category"].lower():
                score += 2

            if word in tool["description"].lower():
                score += 2

            if word in searchable_text:
                score += 1

        if score > 0:
            results.append((score, tool))

    results.sort(reverse=True, key=lambda x: x[0])

    return [tool for score, tool in results[:top_k]]