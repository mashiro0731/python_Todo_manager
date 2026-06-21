from datetime import datetime


class Task:
    def __init__(self, title, due_date, priority=3):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def update_priority(self, priority):
        if self._validate_priority(priority):
            self.priority = priority

    def _validate_priority(self, priority):
        return 1 <= priority <= 5

    def get_info(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }