import json
import os

TASKS_FILE = 'tasks.json'

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Show all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task title cannot be empty.")

# Delete a task by index
def delete_task(tasks):
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark a task as done
def mark_done(tasks):
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print(f"Marked as done: {tasks[idx]['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
