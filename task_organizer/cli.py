import click
import pandas as pd
from dateutil import parser
from datetime import datetime
from pathlib import Path
from task_organizer.storage import load_tasks

DATA_FILE = Path("data.json")

@click.group()
def cli():
    """Organizador de tarefas simples."""
    pass

@cli.command()
@click.argument("descricao")
@click.option("--data", "-d", default=str(datetime.now()), help="Data da tarefa")
def add(descricao, data):
    """Adiciona uma nova tarefa com descrição e data."""
    try:
        data_convertida = parser.parse(data)
    except Exception:
        click.echo("Formato de data inválido. Use AAAA-MM-DD.")
        return

    nova_tarefa = {"descricao": descricao, "data": data_convertida.isoformat()}

    if DATA_FILE.exists():
        df = pd.read_json(DATA_FILE)
    else:
        df = pd.DataFrame(columns=["descricao", "data"])

    df = pd.concat([df, pd.DataFrame([nova_tarefa])], ignore_index=True)
    df.to_json(DATA_FILE, orient="records", indent=2)
    click.echo("Tarefa adicionada com sucesso!")

@cli.command()
def list():
    """Lista todas as tarefas."""
    tasks = load_tasks()
    if not tasks:
        click.echo("Nenhuma tarefa encontrada.")
        return
    for i, task in enumerate(tasks, start=1):
        click.echo(f"{i}. {task['descricao']} - {task['data']}")
