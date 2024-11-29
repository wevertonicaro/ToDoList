class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task.strip():
            self.tasks.append(task)
            return True
        return False

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def get_tasks(self):
        return self.tasks