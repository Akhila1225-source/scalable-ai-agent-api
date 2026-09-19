from app.tools import get_payment, create_payment, refund_payment, get_customer
from app.search import search_tools
from app.rag import search_knowledge
from app.system_search import system_search
from app.state import AgentState

state = AgentState()


def run_agent(user_input, value=None):
    try:
        state.set("user_request", user_input)

        query = user_input.lower()

        # RAG Pipeline Tool
        if "what is" in query or "explain" in query or "how does" in query:
            result = search_knowledge(user_input)
            state.set("selected_tool", "rag_pipeline")
            state.add_execution("rag_pipeline", result)
            return result

        # System Search Tool
        if (
            "available tools" in query
            or "system search" in query
            or "list tools" in query
        ):
            result = system_search(user_input)
            state.set("selected_tool", "system_search")
            state.add_execution("system_search", result)
            return result

        # Direct intent handling for supported PayPal operations
        if "refund" in query:
            selected_tool = "refund_payment"

        elif "create" in query and "payment" in query:
            selected_tool = "create_payment"

        elif "customer" in query:
            selected_tool = "get_customer"

        elif "payment" in query:
            selected_tool = "get_payment"

        else:
            # Search the API catalog for other requests
            tools = search_tools(user_input)

            if not tools:
                return "Sorry, I could not find a suitable PayPal API."

            selected_tool = tools[0]["name"]

        state.set("selected_tool", selected_tool)

        # Execute selected tool
        if selected_tool == "get_payment":
            if not value:
                return "Payment ID is required."

            state.set("payment_id", value)
            result = get_payment(value)

        elif selected_tool == "create_payment":
            if not value:
                return "Amount is required."

            state.set("amount", value)
            result = create_payment(value)

        elif selected_tool == "refund_payment":
            if not value:
                return "Payment ID is required."

            state.set("payment_id", value)
            result = refund_payment(value)

        elif selected_tool == "get_customer":
            if not value:
                return "Customer ID is required."

            state.set("customer_id", value)
            result = get_customer(value)

        else:
            return {
                "message": "The tool was found in the catalog but its execution is not implemented yet.",
                "selected_tool": selected_tool
            }

        state.add_execution(selected_tool, result)

        return result

    except Exception as error:
        return {
            "error": "Tool execution failed",
            "details": str(error)
        }


if __name__ == "__main__":
    user_input = input("What do you want to do? ")

    if "refund" in user_input.lower():
        value = input("Enter payment ID: ")

    elif "create" in user_input.lower() and "payment" in user_input.lower():
        value = input("Enter amount: ")

    elif "customer" in user_input.lower():
        value = input("Enter customer ID: ")

    elif "what is" in user_input.lower() or "explain" in user_input.lower():
        value = None

    elif (
        "available tools" in user_input.lower()
        or "system search" in user_input.lower()
        or "list tools" in user_input.lower()
    ):
        value = None

    else:
        value = input("Enter payment ID: ")

    result = run_agent(user_input, value)

    print("Agent Response:")
    print(result)
    print("Stored Request:", state.get("user_request"))
    print("Selected Tool:", state.get("selected_tool"))