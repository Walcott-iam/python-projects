tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            number = int(input("Task number to remove: "))
            tasks.pop(number - 1)
            print("Task removed")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")