import csv


def save_tasks(tasks, filename):
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


def load_tasks(filename):
    tasks = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tasks.append(row)

    return tasks