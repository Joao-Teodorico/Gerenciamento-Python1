import csv
from pathlib import Path

FILE_PATH = Path("tasks.csv")

def save_tasks(tasks):
    with open(FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["titulo", "descricao", "data", "concluida"])
        writer.writeheader()
        for task in tasks:
            task_copy = task.copy()
            task_copy["concluida"] = str(task_copy["concluida"])
            writer.writerow(task_copy)

def load_tasks():
    tasks = []
    try:
        with open(FILE_PATH, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["concluida"] = row["concluida"].lower() == 'true'
                tasks.append(row)
    except FileNotFoundError:
        pass
    return tasks