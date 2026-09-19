class AgentState:
    def __init__(self):
        self.data = {
            "user_request": None,
            "selected_tool": None,
            "execution_history": []
        }

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def add_execution(self, tool_name, result):
        self.data["execution_history"].append({
            "tool": tool_name,
            "result": result
        })

    def get_history(self):
        return self.data["execution_history"]