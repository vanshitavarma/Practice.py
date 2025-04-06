# Initialize an empty to-do list
todo_list = []

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    # Get user choice
    choice = int(input("Enter your choice: "))

    # Using match-case (available in Python 3.10+)
    match choice:
        case 1:
            task = input("Enter the task to add: ")
            todo_list.append(task)
            print(f"Task '{task}' added successfully!")

        case 2:
            if not todo_list:
                print("No tasks in the to-do list.")
            else:
                print("\nYour To-Do List:")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")

        case 3:
            if not todo_list:
                print("No tasks to remove.")
            else:
                print("\nYour To-Do List:")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")

                task_no = int(input("Enter the task number to remove: "))
                if 1 <= task_no <= len(todo_list):
                    removed_task = todo_list.pop(task_no - 1)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number!")

        case 4:
            print("Exiting... Have a great day!")
            break

        case _:
            print("Invalid choice! Please enter a valid option.")
