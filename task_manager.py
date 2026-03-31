def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!\n")


def mark_complete(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index] = tasks[index] + " [Done]"
            print("Task marked as complete!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input.\n")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input.\n")


def menu():
    tasks = load_tasks()

    while True:
        print("==== Task Manager ====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Run program
menu()
