import csv


def save_tasks(tasks: list, filename: str):
    """할 일 객체 리스트를 CSV 파일로 저장합니다.

    :param tasks: Task 또는 RecurringTask 객체들이 담긴 리스트
    :param filename: 저장할 CSV 파일의 경로 및 이름

    사용 예시:
    >>> from datetime import datetime
    >>> from todo_package import Task  # 실제 패키지명에 맞게 수정 가능
    >>> task_list = [Task("테스트 할 일", datetime(2026, 6, 22), priority=2)]
    >>> save_tasks(task_list, "test_tasks.csv")
    """
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["title", "due_date", "priority", "completed"]
        )

        for task in tasks:
            writer.writerow([
                task.title,
                task.due_date,
                task.priority,
                task.completed
            ])


def load_tasks(filename: str) -> list:
    """CSV 파일로부터 할 일 데이터를 읽어와 딕셔너리 리스트로 반환합니다.

    :param filename: 읽어올 CSV 파일의 경로 및 이름
    :return: 각 할 일의 데이터가 딕셔너리 형태로 담긴 리스트

    사용 예시:
    >>> # 'test_tasks.csv' 파일이 존재하는 경우
    >>> data = load_tasks("test_tasks.csv")
    >>> isinstance(data, list)
    True
    """
    tasks = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tasks.append(row)

    return tasks
