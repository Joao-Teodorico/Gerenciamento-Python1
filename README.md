# Gerenciamento-Python1
# 📋 Organizador de Tarefas - CLI com Python

Um aplicativo de linha de comando (CLI) simples e funcional para organizar tarefas usando Python, arquivos CSV e a biblioteca `click`.

## ✅ Funcionalidades

- ✅ Adicionar tarefas com título, descrição e data de vencimento
- ✅ Listar tarefas pendentes ou concluídas
- ✅ Marcar tarefas como concluídas
- ✅ Remover tarefas individualmente
- ✅ Limpar todas as tarefas
- ✅ Persistência de dados em CSV
- ✅ Teste básico de escrita/leitura

---

## 🚀 Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd Gerenciamento-Python1
Instale o Poetry (se ainda não tiver):

bash
Copy
Edit
pip install poetry
Instale as dependências:

bash
Copy
Edit
poetry install

🛠️ Como usar
Executar comandos:
Todos os comandos são executados com:

bash
Copy
Edit
poetry run python main.py [comando] [opções]
Comandos disponíveis:
➕ Adicionar tarefa
bash
Copy
Edit
poetry run python main.py add "Estudar Python" --descricao "Revisar conceitos" --data 2025-06-01

📋 Listar tarefas
Pendentes (padrão):

bash
Copy
Edit
poetry run python main.py list
Concluídas:

bash
Copy
Edit
poetry run python main.py list --concluidas

✔️ Marcar tarefa como concluída
bash
Copy
Edit
poetry run python main.py complete 1

❌ Remover uma tarefa
bash
Copy
Edit
poetry run python main.py remove 1

🧹 Limpar todas as tarefas
bash
Copy
Edit
poetry run python main.py clear

🧪 Testes
Teste básico de leitura e escrita com CSV:

bash
Copy
Edit
poetry run python -m task_organizer.test_storage

📁 Estrutura de Arquivos
bash
Copy
Edit
Gerenciamento-Python1/
├── task_organizer/
│   ├── cli.py           # CLI principal
│   ├── storage.py       # Leitura/Gravação CSV
│   └── test_storage.py  # Teste funcional
├── main.py              # Entrada principal
├── tasks.csv            # Arquivo com as tarefas (gerado automaticamente)
├── pyproject.toml       # Configuração do Poetry
├── README.md            # Este arquivo

📦 Dependências
Click

python-dateutil

Instaladas automaticamente com o Poetry.

🧑‍💻 Autor
Desenvolvido por João – projeto educativo para praticar Python, CLI e organização de código.
