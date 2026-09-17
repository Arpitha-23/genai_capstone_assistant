class AgentState:

    def __init__(self):

        self.messages = []

        self.last_tool_used = None


    # ========================================================
    # ADD MESSAGE
    # ========================================================

    def add_message(
        self,
        role,
        content
    ):

        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )


    # ========================================================
    # GET HISTORY
    # ========================================================

    def get_history(self):

        return self.messages


    # ========================================================
    # SET LAST TOOL
    # ========================================================

    def set_tool_used(
        self,
        tool_name
    ):

        self.last_tool_used = tool_name


    # ========================================================
    # CLEAR STATE
    # ========================================================

    def clear(self):

        self.messages = []

        self.last_tool_used = None