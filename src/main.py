import polars as pl

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(title)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task index.")

    def show_tasks(self):
        print("Your Tasks:")
        for i, tasks in enumerate(self.tasks, start=1):
            print(f"{i}. {tasks}")

if __name__ == "__main__":
    todo = Todo()
    todo.add_task("Learn Python classes")
    todo.add_task("Run code inside Docker")
    todo.show_tasks()