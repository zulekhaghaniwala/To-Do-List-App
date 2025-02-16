# Simple To-Do List App

tasks = []  # List to store tasks

def display_tasks():
    """Show the current tasks."""
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task():
    """Add a task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    """Remove a task from the list."""
    display_tasks()
    try:
        task_num = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Deleted task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List app."""
    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
