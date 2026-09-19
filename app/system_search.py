import json

def system_search(query):
    with open("data/api_catalog.json", "r") as file:
        tools = json.load(file)

    query = query.lower()

    # If the user asks to list all available tools
    if (
        "list available tools" in query
        or "available tools" in query
        or "list tools" in query
    ):
        results = tools

    else:
        results = []

        for tool in tools:
            text = (
                tool["name"] + " " +
                tool["category"] + " " +
                tool["description"]
            ).lower()

            if any(word in text for word in query.split()):
                results.append(tool)

    if not results:
        return {
            "message": "No matching system tools found."
        }

    return {
        "tools_found": len(results),
        "tools": [
            {
                "name": tool["name"],
                "category": tool["category"],
                "method": tool["method"],
                "endpoint": tool["endpoint"]
            }
            for tool in results
        ]
    }