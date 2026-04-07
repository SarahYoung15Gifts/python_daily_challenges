class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)
        return f"Task '{task_name}' added."

    def show_tasks(self):
        if not self.tasks:
            return ["No tasks yet!"]
        return ["Tasks:"] + [f"{idx}. {task}" for idx, task in enumerate(self.tasks, 1)]

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            return f"Task '{removed_task}' removed."
        return "Invalid task index."


def run_task_manager(reader=None, writer=None):
    reader = reader or input
    writer = writer or print
    task_manager = TaskManager()

    while True:
        choice = reader("Choose: (1) Add Task (2) Show Tasks (3) Remove Task (4) Exit\n")

        if choice == "1":
            task_name = reader("Enter task name: ")
            writer(task_manager.add_task(task_name))
        elif choice == "2":
            for line in task_manager.show_tasks():
                writer(line)
        elif choice == "3":
            try:
                task_index = int(reader("Enter task number you would like to remove: ")) - 1
                writer(task_manager.remove_task(task_index))
            except ValueError:
                writer("Please enter a number only.")
        elif choice == "4":
            writer("Goodbye!")
            break
        else:
            writer("Invalid choice. Try again.")


def main():
    run_task_manager()


if __name__ == "__main__":
    main()

#script to run the code: python day_20_task_manager_cli.py