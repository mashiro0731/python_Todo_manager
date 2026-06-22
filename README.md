Python 기말 프로젝트

주제: 할 일 관리 도구 'Todo manager'

개요: Todo Manager는 Python으로 구현한 할 일 관리 패키지입니다. 사용자는 할 일을 생성하고, 우선순위를 설정하고 완료 상태를 관리할 수 있습니다. 또한 반복 작업 관리 기능과 CSV 파일을 이용한 저장 및 불러오기 기능을 제공합니다.

설치 방법:프로젝트를 다운로드한 후 프로젝트 루트 디렉터리에서 다음 명령을 실행합니다.

pip install -e .

필요한 패키지를 설치하려면 다음 명령을 실행합니다.

pip install -r requirements.txt

빠른 설치:
from datetime import datetime
from todo_manager import Task, TaskManager

manager = TaskManager()

task = Task(
    "파이썬 과제 제출",
    datetime(2026, 6, 22),
    priority=2
)

manager.add_task(task)

print(manager.show_tasks())

주요 기능 설명:

Task 클래스

1. 할 일 생성
2. 우선순위 설정 및 수정
3. 완료 상태 변경
4. 할 일 정보 조회

RecurringTask 클래스

1. Task 클래스 상속
2. 반복 작업 관리
3. 반복 주기 조회
4. 반복 주기 변경

TaskManager 클래스

1. 할 일 추가
2. 할 일 삭제
3. 할 일 검색
4. 전체 할 일 조회
5. 할 일 완료 처리

CSV 저장 및 불러오기

1. save_tasks() 함수를 이용한 CSV 저장
2. load_tasks() 함수를 이용한 CSV 데이터 불러오기

테스트 실행 방법:
pytest를 이용하여 테스트 수행 결과를 확인 할 수 있습니다

pytest

작성자: 202620845 김시헌

Github URL: https://github.com/mashiro0731/python_Todo_manager
