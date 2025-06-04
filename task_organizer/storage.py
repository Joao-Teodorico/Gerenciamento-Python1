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

# from storage import load_tasks, save_tasks
from storage import load_tasks, save_tasks
# from example_tasks import tasks

# Salva as tarefas no CSV
save_tasks(tasks)

# Carrega as tarefas do CSV
loaded_tasks = load_tasks()

print("Tarefas carregadas:")
for t in loaded_tasks:
    print(t)
