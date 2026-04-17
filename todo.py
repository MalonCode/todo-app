tasks = []

def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def load_tasks():
    try:
        file = open("tasks.txt", "r")
        for line in file:
            tasks.append(line.strip())
        file.close()
    except:
        pass

load_tasks()

while True:
    print("WELCOME TO MY TO-DO LIST APP")
    print("********************************")
    print("1.View task")
    print("2.Add a task")
    print("3.Mark a task as done")
    print("4.Delete a task")
    print("5.Quit")

    choice = input("Enter your choice(1-5):")

    if choice == "5":
        print("Goodbye!")
        break
    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append(task)
        save_tasks()
        print("Task added!")
    elif choice == "1":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks):
                print(i + 1, "-", task)
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks):
                print(i + 1, "-", task)
            number = int(input("Enter task number to mark as done: "))
            tasks[number - 1] = "✓ " + tasks[number - 1]
            save_tasks()
            print("Task marked as done!")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks):
                print(i + 1, "-", task)
            number = int(input("Enter task number to delete: "))
            tasks.pop(number - 1)
            save_tasks()
            print("Task deleted!") 