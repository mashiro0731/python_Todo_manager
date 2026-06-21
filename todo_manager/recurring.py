from .core import Task


class RecurringTask(Task):
    def __init__(self, title, due_date, repeat_cycle, priority=3):
        super().__init__(title, due_date, priority)
        self.repeat_cycle = repeat_cycle

    def get_repeat_cycle(self):
        return self.repeat_cycle

    def change_repeat_cycle(self, new_cycle):
        self.repeat_cycle = new_cycle

    def get_task_type(self):
        return "Recurring Task"