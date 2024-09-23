task_variable = input("Please describe the task: ")
task_priority = input(" please select the priority (High, medium or low): ")
time_bound_variable = input(" what the time bound (yes/no): ")

message = f"Reminder: '{task_variable}' is a {task_priority}"

match task_priority:
    case "high":
        message += " This task requires high attention."
    case "medium":
        message += " This task requires medium attention."
    case "low":
        message += " This task requires low attention."
    case _:
        message += " Invalid priority entered."

if time_bound_variable == "yes":
    if task_priority in ["high", "medium", "low"]:
        message = f"Reminder: '{task_variable}' is a {task_priority} priority task that requires immediate attention today!"
elif time_bound_variable == "no":
    if task_priority in ["high", "medium", "low"]:
        message += " You can take your time."

print(message)

