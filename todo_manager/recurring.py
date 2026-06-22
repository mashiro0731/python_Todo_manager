from datetime import datetime
from .task import Task


class RecurringTask(Task):
    """반복되는 할 일을 관리하는 자식 클래스입니다.

    부모 클래스(Task)의 속성을 상속받으며, 반복 주기 속성이 추가되었습니다.

    :ivar title: 할 일의 제목
    :ivar due_date: 마감 기한 (datetime 객체)
    :ivar repeat_cycle:
        반복 주기 (예: 'Daily', 'Weekly', 'Monthly')
    :ivar priority:
        우선순위 (1~5 사이의 정수, 기본값 3)
    :ivar completed: 완료 여부 (기본값 False)

    사용 예시:
    >>> from datetime import datetime
    >>> rec_task = RecurringTask("주간 회의", datetime(2026, 6, 22), "Weekly")
    >>> rec_task.repeat_cycle
    'Weekly'
    >>> rec_task.get_task_type()
    'Recurring Task'
    """

    def __init__(
        self,
        title: str,
        due_date: datetime,
        repeat_cycle: str,
        priority: int = 3,
    ):
        """RecurringTask 객체를 초기화합니다.

        부모 클래스의 생성자를 super()로 호출하여 기본 속성을 초기화합니다.

        :param title: 할 일의 제목
        :param due_date: 첫 마감 기한
        :param repeat_cycle: 반복 주기 문자열
        :param priority: 우선순위 (1~5)
        """
        super().__init__(title, due_date, priority)
        self.repeat_cycle = repeat_cycle

    def get_repeat_cycle(self) -> str:
        """현재 설정된 반복 주기를 반환합니다.

        :return: 반복 주기 문자열

        사용 예시:
        >>> rec_task = RecurringTask("청소", datetime(2026, 6, 22), "Daily")
        >>> rec_task.get_repeat_cycle()
        'Daily'
        """
        return self.repeat_cycle

    def change_repeat_cycle(self, new_cycle: str):
        """반복 주기를 새로운 값으로 변경합니다.

        :param new_cycle: 새로 지정할 반복 주기 문자열

        사용 예시:
        >>> rec_task = RecurringTask("청소", datetime(2026, 6, 22), "Daily")
        >>> rec_task.change_repeat_cycle("Weekly")
        >>> rec_task.get_repeat_cycle()
        'Weekly'
        """
        self.repeat_cycle = new_cycle

    def get_task_type(self) -> str:
        """해당 태스크의 종류를 문자열로 반환합니다.

        :return: 태스크 타입 이름 ('Recurring Task')

        사용 예시:
        >>> rec_task = RecurringTask("청소", datetime(2026, 6, 22), "Daily")
        >>> rec_task.get_task_type()
        'Recurring Task'
        """
        return "Recurring Task"
