from datetime import datetime

from todo_manager import Task, RecurringTask, TaskManager


def test_task_creation():
    task = Task("과제", datetime(2026, 6, 22), priority=2)

    assert task.title == "과제"
    assert task.priority == 2
    assert task.completed is False


def test_task_mark_complete():
    task = Task("운동", datetime(2026, 6, 22))

    task.mark_complete()

    assert task.completed is True


def test_task_update_priority_valid():
    task = Task("독서", datetime(2026, 6, 22), priority=3)

    task.update_priority(1)

    assert task.priority == 1


def test_task_update_priority_invalid():
    task = Task("독서", datetime(2026, 6, 22), priority=3)

    task.update_priority(10)

    assert task.priority == 3


def test_recurring_task_creation():
    task = RecurringTask("회의", datetime(2026, 6, 22), "Weekly")

    assert task.title == "회의"
    assert task.get_repeat_cycle() == "Weekly"


def test_recurring_task_change_cycle():
    task = RecurringTask("청소", datetime(2026, 6, 22), "Daily")

    task.change_repeat_cycle("Monthly")

    assert task.get_repeat_cycle() == "Monthly"


def test_task_manager_add_and_find_task():
    manager = TaskManager()
    task = Task("시험공부", datetime(2026, 6, 22))

    manager.add_task(task)
    found = manager.find_task("시험공부")

    assert found == task


def test_task_manager_remove_task():
    manager = TaskManager()
    task = Task("삭제할 일", datetime(2026, 6, 22))

    manager.add_task(task)

    assert manager.remove_task("삭제할 일") is True
    assert manager.find_task("삭제할 일") is None


def test_task_manager_complete_task():
    manager = TaskManager()
    task = Task("코딩", datetime(2026, 6, 22))

    manager.add_task(task)

    assert manager.complete_task("코딩") is True
    assert task.completed is True