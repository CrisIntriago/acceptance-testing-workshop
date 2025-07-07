import sys
from todo_list import TodoList

def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Clear all tasks")
    print("5. Update a task")
    print("6. Delete a task")
    print("7. Exit")

def main():
    todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low, Medium, High): ")
            todo_list.add_task(title, description, due_date, priority)
            print(f"Task '{title}' added to the to-do list.")

        elif choice == "2":
            print("\nList of tasks:")
            tasks = todo_list.list_tasks()
            print(tasks)

        elif choice == "3":
            title = input("Enter the task title to mark as completed: ")
            result = todo_list.mark_task_completed(title)
            print(result)

        elif choice == "4":
            result = todo_list.clear_all_tasks()
            print(result)

        elif choice == "5":
            title = input("Enter the task title to update: ")
            new_title = input("Enter new title (press enter to skip): ") or None
            description = input("Enter new description (press enter to skip): ") or None
            due_date = input("Enter new due date (press enter to skip): ") or None
            priority = input("Enter new priority (press enter to skip): ") or None
            result = todo_list.update_task(title, new_title, description, due_date, priority)
            print(result)

        elif choice == "6":
            title = input("Enter the task title to delete: ")
            result = todo_list.delete_task(title)
            print(result)

        elif choice == "7":
            print("Exiting To-Do List Manager. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
