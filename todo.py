import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        tasks = json.load(f)
    # Migrate old format if necessary
    for i, task in enumerate(tasks):
        if isinstance(task, str):
            tasks[i] = {
                'task': task,
                'status': 'pending',
                'priority': 'medium',
                'due_date': None
            }
    return tasks


def save_tasks(tasks):
    
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def show_menu():
    
    print("\n=== TO-DO LIST APP ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task Complete")
    print("5. Edit Task")
    print("6. Search Tasks")
    print("7. Exit")


def view_tasks():
    
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = task.get('status', 'pending')
            priority = task.get('priority', 'medium')
            due_date = task.get('due_date', 'No due date')
            task_text = task.get('task', task)  # Handle old format
            print(f"{i}. [{status.upper()}] {task_text} (Priority: {priority}, Due: {due_date})")


def add_task():
    
    task_text = input("Enter new task: ").strip()
    if not task_text:
        print("Task cannot be empty!")
        return

    
    while True:
        priority = input("Enter priority (low/medium/high): ").strip().lower()
        if priority in ['low', 'medium', 'high']:
            break
        print("Invalid priority. Please choose low, medium, or high.")

    
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    if due_date:
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Using no due date.")
            due_date = None

    task = {
        'task': task_text,
        'status': 'pending',
        'priority': priority,
        'due_date': due_date if due_date else None
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")


def delete_task():
    tasks = load_tasks()
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: "))
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed}")
    except:
        print("Invalid choice!")


def main():
    
    while True:
        show_menu()
        choice = input("\nChoose option: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_complete()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            search_tasks()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
