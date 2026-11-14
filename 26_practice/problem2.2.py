# Open tasks.txt in append mode and add a new line "Task Completed!".

with open("tasks.txt", "a") as f:
    f.write("Task Completed!")