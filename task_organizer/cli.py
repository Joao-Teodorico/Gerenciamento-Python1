import click
from dateutil import parser
from datetime import datetime
from task_organizer.storage import load_tasks, save_tasks

@click.group()
def cli():
    """Organizador de Tarefas em CSV"""
    pass
@cli.command()
@click.argument("titulo")
@click.option("--descricao", "-d", default="", help="Descrição da tarefa")
@click.option("--data", "-D", default=str(datetime.now().date()), help="Data de vencimento (AAAA-MM-DD)")
def add(titulo, descricao, data):
    """Adiciona uma nova tarefa."""
    try:
        data_convertida = parser.parse(data).date()
    except Exception:
        click.echo("Formato de data inválido. Use AAAA-MM-DD.")
        return
    
    tasks = load_tasks()
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "data": data_convertida.isoformat(),
        "concluida": False
    }
    tasks.append(nova_tarefa)
    save_tasks(tasks)
    click.echo("Tarefa adicionada com sucesso!")
@cli.command()
@click.option("--concluidas", is_flag=True, help="Mostrar somente tarefas concluídas")
def list(concluidas):
    """Lista tarefas (pendentes por padrão)."""
    tasks = load_tasks()
    filtradas = [t for t in tasks if t["concluida"] == concluidas]
    if not filtradas:
        click.echo("Nenhuma tarefa encontrada para esse filtro.")
        return
    for i, task in enumerate(filtradas, start=1):
        status = "✔" if task["concluida"] else "✘"
        click.echo(f"{i}. [{status}] {task['titulo']} - {task['descricao']} (Vence em {task['data']})")

@cli.command()
@click.argument("index", type=int)
def complete(index):
    """Marca a tarefa como concluída pelo índice da listagem pendente."""
    tasks = load_tasks()
    pendentes = [t for t in tasks if not t["concluida"]]
    if index < 1 or index > len(pendentes):
        click.echo("Índice inválido.")
        return
    tarefa = pendentes[index - 1]
    tarefa["concluida"] = True
    save_tasks(tasks)
    click.echo(f"Tarefa '{tarefa['titulo']}' marcada como concluída!")
