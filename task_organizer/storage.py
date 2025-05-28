import csv
from pathlib import Path

DATA_FILE = Path("tasks.csv")
FIELDNAMES = ["titulo", "descricao", "data", "concluida"]

def load_tasks():
    tasks = []
    if not DATA_FILE.exists():
        return tasks
    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["concluida"] = row["concluida"].lower() == 'true'
            tasks.append(row)
    return tasks

def save_tasks(tasks):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for task in tasks:
            task_to_save = task.copy()
            task_to_save["concluida"] = str(task_to_save["concluida"])
            writer.writerow(task_to_save)
