# List to hold all tasks
tasks = []

# Function to add a task
def add_task():
    """
    Prompts the user to enter a new task and adds it to the tasks list.
    """
    task = input("Enter a new task: ")  # Get task input from the user
    tasks.append(task)  # Add the task to the list
    print(f"Task '{task}' added.")  # Confirm task addition

# Function to view all tasks
def view_tasks():
    """
    Displays all tasks in the tasks list.
    If the list is empty, informs the user.
    """
    if not tasks:  # Check if the list is empty
        print("No tasks in the list.")  # Notify the user
    else:
        print("\nYour Tasks:")  # Header for tasks display
        # Loop through the tasks list and display each task with an index
        for i, task in enumerate(tasks, 1):  # Start index at 1 for user-friendly numbering
            print(f"{i}. {task}")

# Main program loop
while True:
    # Display the main menu
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Quit")

    # Prompt the user for a choice
    choice = input("Enter your choice (1-3): ")

    # Handle user input based on their choice
    if choice == "1":
        add_task()  # Call the function to add a task
    elif choice == "2":
        view_tasks()  # Call the function to view tasks
    elif choice == "3":
        print("Goodbye!")  # Farewell message
        break  # Exit the loop and terminate the program
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")  # Handle invalid input
