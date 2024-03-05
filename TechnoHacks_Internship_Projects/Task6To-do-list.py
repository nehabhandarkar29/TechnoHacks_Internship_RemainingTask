class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Function to add a task to the to-do list"""
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task_index):
        """Function to remove a task from the to-do list"""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        """Function to display all tasks in the to-do list"""
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            if todo_list.tasks:
                index = int(input("Enter the index of the task to remove: ")) - 1
                todo_list.remove_task(index)
            else:
                print("No tasks to remove. Your to-do list is empty.")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Thank you for using the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
