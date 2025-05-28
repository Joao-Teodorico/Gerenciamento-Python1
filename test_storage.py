from storage import load_tasks, save_tasks

# Cria algumas tarefas de exemplo
tasks = [
    {"titulo": "Tarefa 1", "descricao": "Descrição 1", "data": "2025-06-01", "concluida": False},
    {"titulo": "Tarefa 2", "descricao": "Descrição 2", "data": "2025-06-02", "concluida": True}
]

# Salva as tarefas no CSV
save_tasks(tasks)

# Carrega as tarefas do CSV
loaded_tasks = load_tasks()

print("Tarefas carregadas:")
for t in loaded_tasks:
    print(t)
