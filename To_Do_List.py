import os

def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

def add_task(filename, task):
    with open(filename, 'a') as file:
        file.write(task + '\n')

def view_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.readlines()
        if tasks:
            print("\nTo-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")
    else:
        print("No tasks file found.")

def delete_task(filename, task_number):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
            with open(filename, 'w') as file:
                file.writelines(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks file found.")

def main():
    filename = 'todo_list.txt'
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the new task: ")
            add_task(filename, task)
        elif choice == '2':
            view_tasks(filename)
        elif choice == '3':
            view_tasks(filename)
            task_number = int(input("Enter the task number to delete: "))
            delete_task(filename, task_number)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
