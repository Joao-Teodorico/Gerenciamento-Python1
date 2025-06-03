from storage import load_tasks, save_tasks
tasks = [
    {"titulo": "Tarefa 1", "descricao": "Descrição 1", "data": "2025-06-01", "concluida": False},
    {"titulo": "Tarefa 2", "descricao": "Descrição 2", "data": "2025-06-02", "concluida": True}
]
save_tasks(tasks)
