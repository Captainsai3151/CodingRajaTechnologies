import json
import os
import datetime
import matplotlib.pyplot as plt

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to load tasks from file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks
def display_tasks(tasks):
    clear_screen()
    print("To-Do List\n")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")
    else:
        print("No tasks found.")




# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter task priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({'title': title, 'priority': priority, 'due_date': due_date, 'completed': False})
    save_tasks(tasks)
    print("Task added successfully!")

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the index of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task index.")

# Function to mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def display_task_analysis(tasks):
    categories = [task['priority'] for task in tasks]
    priority_counts = {priority: categories.count(priority) for priority in ['high', 'medium', 'low']}  # Explicitly set the order of priority levels
    plt.figure(figsize=(8, 6))
    bars = plt.bar(priority_counts.keys(), priority_counts.values(), color=['red', 'orange', 'Green'])  # Assign colors to bars
    plt.title('Task Priority Analysis')
    plt.xlabel('Priority')
    plt.ylabel('Number of Tasks')
    plt.show()

# Main function
def main():
    tasks = load_tasks()

    while True:
        clear_screen()
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_tasks(tasks)
            input("Press Enter to continue...")
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            print("Exiting...")
            display_task_analysis(tasks)  # Call the function to display task analysis
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()