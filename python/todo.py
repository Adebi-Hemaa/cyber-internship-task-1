import os
# File to store tasks
TODO_FILE = "todo_list.txt"

def load_tasks():
    """Load tasks from the file."""
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = [line.strip() for line in file if line.strip()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks in the list!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def update_task(tasks):
    """Update an existing task."""
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter the new task description: ").strip()
                if new_task:
                    tasks[index] = new_task
                    save_tasks(tasks)
                    print(f"Task {index + 1} updated successfully!")
                else:
                    print("Task description cannot be empty!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                save_tasks(tasks)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    
    while True:
        print("\n=== To-Do List Application ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()