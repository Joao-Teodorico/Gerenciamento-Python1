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
