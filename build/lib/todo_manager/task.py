from datetime import datetime


class Task:
    """할 일을 관리하는 기본 클래스입니다.

    :ivar title: 할 일의 제목
    :ivar due_date: 마감 기한 (datetime 객체 또는 문자열)
    :ivar priority: 우선순위 (1~5 사이의 정수, 기본값 3)
    :ivar completed: 완료 여부 (기본값 False)

    사용 예시:
    >>> from datetime import datetime
    >>> task = Task("과제 제출하기", datetime(2026, 6, 22), priority=1)
    >>> task.priority
    1
    >>> task.completed
    False
    >>> task.mark_complete()
    >>> task.completed
    True
    """

    def __init__(self, title: str, due_date: datetime, priority: int = 3):
        """Task 객체를 초기화합니다.

        :param title: 할 일의 제목
        :param due_date: 마감 기한
        :param priority: 우선순위 (1~5, 숫자가 작을수록 높은 우선순위)
        """
        self.title = title
        self.due_date = due_date

        if self._validate_priority(priority):
            self.priority = priority
        else:
            self.priority = 3

        self.completed = False

    def mark_complete(self):
        """할 일을 완료 상태로 변경합니다.

        사용 예시:
        >>> task = Task("운동하기", datetime(2026, 6, 22))
        >>> task.mark_complete()
        >>> task.completed
        True
        """
        self.completed = True

    def update_priority(self, priority: int):
        """유효한 범위 내에서 할 일의 우선순위를 변경합니다.

        :param priority: 변경할 우선순위 정수 (1~5)

        사용 예시:
        >>> task = Task("독서하기", datetime(2026, 6, 22), priority=3)
        >>> task.update_priority(5)
        >>> task.priority
        5
        >>> task.update_priority(10)  # 범위를 벗어나면 변경되지 않음
        >>> task.priority
        5
        """
        if self._validate_priority(priority):
            self.priority = priority

    def _validate_priority(self, priority: int) -> bool:
        """우선순위 값이 유효한 범위(1~5)에 있는지 검증합니다 (비공개 메서드).

        :param priority: 검증할 우선순위 값
        :return: 유효 여부 (True/False)
        """
        return 1 <= priority <= 5

    def get_info(self) -> dict:
        """할 일의 현재 모든 정보(속성)를 딕셔너리 형태로 반환합니다.

        :return: 할 일 정보를 담은 딕셔너리

        사용 예시:
        >>> task = Task("테스트", datetime(2026, 6, 22), priority=2)
        >>> info = task.get_info()
        >>> info["title"]
        '테스트'
        >>> info["priority"]
        2
        """
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
        }
