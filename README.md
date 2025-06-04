📋 Task Organizer – Gerenciador de Tarefas em Python

Este projeto é um gerenciador de tarefas simples desenvolvido em Python. Ele permite salvar e carregar tarefas de um arquivo CSV, simulando um pequeno sistema de controle pessoal de atividades.

🚀 Funcionalidades
✅ Adicionar tarefas manualmente (via código)

✅ Salvar tarefas em um arquivo tasks.csv

✅ Carregar tarefas salvas e exibir no terminal

📂 Uso de arquivos CSV como forma de armazenamento simples

🧱 Organização modular com separação de responsabilidades (storage, testes, main)

🧰 Tecnologias e dependências
Python 3.10+ ou 3.13

poetry (como gerenciador de dependências)

Biblioteca padrão do Python (csv, pathlib)

📦 Para instalar as dependências
poetry install

📁 Estrutura de pastas
Gerenciamento-Python1/
├── main.py                    # Arquivo principal (ponto de entrada)
├── tasks.csv                 # Arquivo onde as tarefas são salvas
├── test_storage.py           # Script de teste
├── task_organizer/
│   └── storage.py            # Funções de salvar e carregar tarefas
├── pyproject.toml            # Arquivo de configuração do Poetry
├── README.md                 # Este arquivo


▶️ Como executar
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

Instale o ambiente virtual:
poetry install

Rode o projeto:
poetry run python task_organizer/test_storage.py

Se quiser rodar diretamente sem Poetry:
python task_organizer/test_storage.py
📝 Isso irá salvar tarefas de exemplo no arquivo CSV e imprimi-las no terminal.

✍️ Colaboradores
João Teodorico De Sousa Segundo
Anderson Matheus Correia Souza de Assunção
Isabelly dos Santos Nascimento
