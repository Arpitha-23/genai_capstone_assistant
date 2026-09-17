import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from agent.tools import TOOLS
from agent.state import AgentState


# ============================================================
# LOAD API KEY
# ============================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not configured. "
        "Please add it to your .env file."
    )


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)

MODEL_NAME = "gemini-3.6-flash"


# ============================================================
# TOOL DEFINITIONS
# ============================================================

calculator_function = types.FunctionDeclaration(
    name="calculator",
    description="Perform a mathematical calculation.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "expression": types.Schema(
                type=types.Type.STRING,
                description="Mathematical expression such as 25 * 18."
            )
        },
        required=["expression"]
    )
)


current_time_function = types.FunctionDeclaration(
    name="get_current_time",
    description="Get the current local date and time.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={}
    )
)


add_task_function = types.FunctionDeclaration(
    name="add_task",
    description="Add a task to the user's task list.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "task": types.Schema(
                type=types.Type.STRING,
                description="The task that should be added."
            )
        },
        required=["task"]
    )
)


list_tasks_function = types.FunctionDeclaration(
    name="list_tasks",
    description="List all tasks currently stored.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={}
    )
)


gemini_tools = types.Tool(
    function_declarations=[
        calculator_function,
        current_time_function,
        add_task_function,
        list_tasks_function
    ]
)


# ============================================================
# SYSTEM INSTRUCTION
# ============================================================

SYSTEM_INSTRUCTION = """
You are an AI Task Assistant.

Available tools:

1. calculator
   Use for mathematical calculations.

2. get_current_time
   Use when the user asks for the current date or time.

3. add_task
   Use when the user wants to add a task.

4. list_tasks
   Use when the user wants to see their tasks.

Rules:

- Understand the user's request carefully.
- Use a tool when appropriate.
- Do not pretend that a tool was used if it was not.
- Give short and clear answers.
"""


# ============================================================
# AI AGENT
# ============================================================

class AIAgent:

    def __init__(self):
        self.state = AgentState()


    # ========================================================
    # BUILD HISTORY
    # ========================================================

    def _build_history(self):

        history = []

        for message in self.state.get_history():

            history.append(
                f"{message['role'].upper()}: "
                f"{message['content']}"
            )

        return "\n".join(history)


    # ========================================================
    # EXECUTE TOOL
    # ========================================================

    def _execute_tool(
        self,
        tool_name,
        arguments
    ):

        if tool_name not in TOOLS:

            return f"Unknown tool: {tool_name}"

        try:

            result = TOOLS[tool_name](
                **arguments
            )

            self.state.set_tool_used(
                tool_name
            )

            return result

        except Exception as e:

            return f"Tool execution error: {str(e)}"


    # ========================================================
    # RUN AGENT
    # ========================================================

    def run(self, user_input):

        self.state.add_message(
            "user",
            user_input
        )

        history = self._build_history()

        prompt = f"""
Conversation history:

{history}

Latest user request:

{user_input}
"""

        max_retries = 4

        for attempt in range(max_retries):

            try:

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.2,
                        tools=[gemini_tools]
                    )
                )

                # ==================================================
                # TOOL CALL
                # ==================================================

                if response.function_calls:

                    function_call = response.function_calls[0]

                    tool_name = function_call.name

                    arguments = function_call.args or {}

                    tool_result = self._execute_tool(
                        tool_name,
                        arguments
                    )

                    if tool_name == "calculator":

                        answer = (
                            f"The answer is {tool_result}."
                        )

                    elif tool_name == "get_current_time":

                        answer = (
                            f"The current date and time is "
                            f"{tool_result}."
                        )

                    else:

                        answer = str(tool_result)

                # ==================================================
                # NORMAL RESPONSE
                # ==================================================

                else:

                    answer = response.text

                    if not answer:

                        answer = (
                            "I couldn't generate a response."
                        )

                self.state.add_message(
                    "assistant",
                    answer
                )

                return answer


            except Exception as e:

                error_text = str(e)

                # --------------------------------------------------
                # Temporary connection/API errors
                # --------------------------------------------------

                temporary_error = (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                    or "429" in error_text
                    or "RESOURCE_EXHAUSTED" in error_text
                    or "Server disconnected" in error_text
                    or "server disconnected" in error_text
                    or "disconnected without sending a response"
                    in error_text
                    or "Connection reset" in error_text
                    or "connection" in error_text.lower()
                )

                if temporary_error:

                    if attempt < max_retries - 1:

                        wait_time = 2 ** attempt

                        time.sleep(wait_time)

                        continue

                # --------------------------------------------------
                # Final error
                # --------------------------------------------------

                error_message = (
                    f"Agent error: {error_text}"
                )

                self.state.add_message(
                    "assistant",
                    error_message
                )

                return error_message

        return (
            "The Gemini service is temporarily unavailable. "
            "Please try again."
        )