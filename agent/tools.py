from datetime import datetime


# ============================================================
# TASK STORAGE
# ============================================================

tasks = []


# ============================================================
# CALCULATOR
# ============================================================

def calculator(expression):

    try:

        allowed_characters = (
            "0123456789"
            "+-*/(). "
        )

        if not all(
            character in allowed_characters
            for character in expression
        ):

            return "Invalid mathematical expression."

        result = eval(
            expression,
            {
                "__builtins__": {}
            },
            {}
        )

        return result

    except Exception:

        return "Unable to calculate the expression."


# ============================================================
# CURRENT TIME
# ============================================================

def get_current_time():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# ============================================================
# ADD TASK
# ============================================================

def add_task(task):

    tasks.append(task)

    return (
        f'Task added successfully: "{task}"'
    )


# ============================================================
# LIST TASKS
# ============================================================

def list_tasks():

    if not tasks:

        return "You currently have no tasks."

    result = []

    for index, task in enumerate(
        tasks,
        start=1
    ):

        result.append(
            f"{index}. {task}"
        )

    return "\n".join(result)


# ============================================================
# TOOL REGISTRY
# ============================================================

TOOLS = {

    "calculator": calculator,

    "get_current_time": get_current_time,

    "add_task": add_task,

    "list_tasks": list_tasks,

}