# Simple To-Do List Application

tasks = []

def add_task(task):
    """Adds a new task to the list."""
    tasks.append(task)
    print(f'Task "{task}" added successfully!')

def view_tasks():
    """Displays all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(task_number):
    """Removes a task by its index."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f'Task "{removed}" removed successfully!')
    else:
        print("Invalid task number!")

def main():
    """Main function to run the to-do list program."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
