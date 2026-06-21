class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def show_tasks(self):
        return [task.get_info() for task in self.tasks]
    
    def complete_task(self, title):
        task = self.find_task(title)

        if task:
            task.mark_complete()
            return True

        return False