#from task_organizer.cli import cli

#if __name__ == "__main__":
 #   cli()
from storage import load_tasks, save_tasks
from example_tasks import tasks

# Salva as tarefas no CSV
save_tasks(tasks)

# Carrega as tarefas do CSV
loaded_tasks = load_tasks()

print("Tarefas carregadas:")
for t in loaded_tasks:
    print(t)
