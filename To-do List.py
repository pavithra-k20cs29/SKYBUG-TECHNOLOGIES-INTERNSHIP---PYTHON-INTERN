# Create an empty list to store the tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to display all tasks
def display_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

# Function to update a task
def update_task():
    display_tasks()
    task_index = int(input("Enter the task number to update: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
    else:
        new_task = input("Enter the updated task: ")
        tasks[task_index] = new_task
        print("Task updated successfully!")

# Function to remove a task
def remove_task():
    display_tasks()
    task_index = int(input("Enter the task number to remove: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
    else:
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")

# Main program loop
while True:
    print("\nTO-DO LIST")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")