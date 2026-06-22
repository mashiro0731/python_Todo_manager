class TaskManager:
    """할 일(Task) 객체들을 추가, 삭제, 검색 및 상태 관리하는 매니저 클래스입니다.

    :ivar tasks: 관리하는 할 일 객체들의 리스트

    사용 예시:
    >>> from datetime import datetime
    >>> manager = TaskManager()
    >>> task = Task("파이썬 과제", datetime(2026, 6, 22))
    >>> manager.add_task(task)
    >>> len(manager.tasks)
    1
    """

    def __init__(self):
        """TaskManager 객체를 초기화하며 빈 할 일 리스트를 생성합니다."""
        self.tasks = []

    def add_task(self, task):
        """새로운 할 일 객체를 리스트에 추가합니다.

        :param task: 추가할 Task 또는 RecurringTask 객체

        사용 예시:
        >>> from datetime import datetime
        >>> manager = TaskManager()
        >>> manager.add_task(Task("운동", datetime(2026, 6, 22)))
        """
        self.tasks.append(task)

    def remove_task(self, title: str) -> bool:
        """지정한 제목을 가진 할 일을 찾아 삭제합니다.

        :param title: 삭제할 할 일의 제목
        :return: 삭제 성공 여부 (True/False)

        사용 예시:
        >>> from datetime import datetime
        >>> manager = TaskManager()
        >>> manager.add_task(Task("삭제할일", datetime(2026, 6, 22)))
        >>> manager.remove_task("삭제할일")
        True
        >>> manager.remove_task("없는일")
        False
        """
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def find_task(self, title: str):
        """지정한 제목을 가진 할 일 객체를 검색하여 반환합니다.

        :param title: 검색할 할 일의 제목
        :return: 검색된 Task 객체 (찾지 못하면 None 반환)

        사용 예시:
        >>> from datetime import datetime
        >>> manager = TaskManager()
        >>> manager.add_task(Task("시험공부", datetime(2026, 6, 22)))
        >>> found = manager.find_task("시험공부")
        >>> found.title
        '시험공부'
        >>> manager.find_task("휴식") is None
        True
        """
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def show_tasks(self) -> list:
        """현재 저장된 모든 할 일의 정보 딕셔너리를 리스트로 반환합니다.

        :return: 할 일 정보 딕셔너리들이 담긴 리스트

        사용 예시:
        >>> from datetime import datetime
        >>> manager = TaskManager()
        >>> manager.add_task(Task("알바", datetime(2026, 6, 22)))
        >>> tasks_info = manager.show_tasks()
        >>> tasks_info[0]["title"]
        '알바'
        """
        return [task.get_info() for task in self.tasks]

    def complete_task(self, title: str) -> bool:
        """지정한 제목을 가진 할 일을 완료 상태로 변경합니다.

        :param title: 완료 처리할 할 일의 제목
        :return: 완료 변경 성공 여부 (True/False)

        사용 예시:
        >>> from datetime import datetime
        >>> manager = TaskManager()
        >>> manager.add_task(Task("코딩", datetime(2026, 6, 22)))
        >>> manager.complete_task("코딩")
        True
        >>> manager.show_tasks()[0]["completed"]
        True
        """
        task = self.find_task(title)

        if task:
            task.mark_complete()
            return True

        return False
