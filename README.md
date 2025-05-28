# ✅ Organizador de Tarefas - Python CLI


Este é um **organizador de tarefas simples** que roda no terminal (linha de comando). Você pode **adicionar, listar, marcar como concluída e remover tarefas** que ficam salvas em um arquivo `.csv`.

## ✅ Funcionalidades

- ✅ Adicionar tarefas com título, descrição e data de vencimento
- ✅ Listar tarefas pendentes ou concluídas
- ✅ Marcar tarefas como concluídas
- ✅ Remover tarefas individualmente
- ✅ Limpar todas as tarefas
- ✅ Persistência de dados em CSV
- ✅ Teste básico de escrita/leitura

## 📦 O que você precisa?

- Python 3.8 ou superior (recomendado: Python 3.10+)
- Git instalado (opcional)
- [Poetry](https://python-poetry.org/docs/) para instalar as dependências (veja abaixo)

---

## 🚀 Como começar passo a passo

### 1. Baixe ou clone o projeto

Com Git:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd Gerenciamento-Python1
Ou baixe o ZIP do projeto e extraia.

2. Instale o Poetry (caso não tenha)
bash
Copy
Edit
pip install poetry
3. Instale as dependências do projeto
Dentro da pasta do projeto:

bash
Copy
Edit
poetry install
🧪 Testar se está funcionando
Rode o teste simples:

bash
Copy
Edit
poetry run python -m task_organizer.test_storage
Se aparecer uma lista de tarefas, está tudo funcionando!

✅ Como usar
Use sempre esse formato:

bash
Copy
Edit
poetry run python main.py [comando] [opções]
▶️ Exemplos:
Adicionar uma tarefa
bash
Copy
Edit
poetry run python main.py add "Estudar Python" --descricao "Revisar conceitos" --data 2025-06-01
Listar tarefas pendentes
bash
Copy
Edit
poetry run python main.py list
Listar tarefas concluídas
bash
Copy
Edit
poetry run python main.py list --concluidas
Marcar uma tarefa como concluída
bash
Copy
Edit
poetry run python main.py complete 1
Remover uma tarefa
bash
Copy
Edit
poetry run python main.py remove 1
Apagar todas as tarefas
bash
Copy
Edit
poetry run python main.py clear
📁 Estrutura dos arquivos
bash
Copy
Edit
Gerenciamento-Python1/
├── main.py                 # Arquivo principal
├── tasks.csv               # Onde as tarefas ficam salvas
├── task_organizer/
│   ├── cli.py              # Código com os comandos
│   ├── storage.py          # Código que salva e carrega o CSV
│   └── test_storage.py     # Teste básico do CSV
├── pyproject.toml          # Configuração do projeto com Poetry
├── README.md               # Este guia
👨‍💻 Autor
Feito por João – projeto educacional para treinar Python e linha de comando.
Fique à vontade para modificar, estudar e usar!

