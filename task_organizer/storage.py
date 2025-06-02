import csv

FILE_PATH = "tasks.csv"

def save_tasks(tasks):
    with open(FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["titulo", "descricao", "data", "concluida"])
        writer.writeheader()
        writer.writerows(tasks)

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
tasks = [
    {"titulo": "Tarefa 1", "descricao": "Descrição 1", "data": "2025-06-01", "concluida": False},
    {"titulo": "Tarefa 2", "descricao": "Descrição 2", "data": "2025-06-02", "concluida": True}
]