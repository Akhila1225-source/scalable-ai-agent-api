def search_knowledge(query):
    knowledge = {
        "paypal": "PayPal is a payment platform that provides APIs for payments, invoices, refunds, customers and disputes.",
        "invoice": "An invoice is a billing document. The system can create, send and retrieve invoice details.",
        "payment": "Payment APIs can be used to create payments, retrieve payment details and process refunds.",
        "dispute": "Dispute APIs provide information about payment disputes and available dispute records.",
        "scalability": "The system uses a searchable tool catalog so that more APIs can be added without changing the core agent logic.",
        "agent": "The agent receives a user request, searches relevant tools, selects a suitable tool and executes it."
    }

    query = query.lower()

    results = []

    for keyword, information in knowledge.items():
        if keyword in query:
            results.append(information)

    if not results:
        return "No relevant information found in the knowledge base."

    return " ".join(results)