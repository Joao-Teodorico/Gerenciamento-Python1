echo "# ✅ Task Organizer – Gerenciador de Tarefas em Python

Este projeto é um gerenciador de tarefas simples, desenvolvido em Python.  
Ele permite salvar e carregar tarefas a partir de um arquivo CSV, simulando um sistema básico de controle de atividades pessoais.

---

## ✨ Funcionalidades

- ➕ Adicionar tarefas manualmente (via código ou script)  
- 💾 Salvar tarefas em um arquivo \`tasks.csv\`  
- 📂 Carregar tarefas salvas e exibir no terminal  
- 🗃️ Armazenamento simples via arquivos CSV  
- Organização modular com separação de responsabilidades (\`storage\`, \`test_storage\`, \`main\`)

---

## 🔧 Tecnologias e Dependências

- Python 3.10+ até 3.13  
- Poetry como gerenciador de dependências  
- Bibliotecas padrão: \`csv\`, \`pathlib\`

---

## 📦 Instalação

\`\`\`bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
poetry install
\`\`\`

---

## ▶️ Como executar

\`\`\`bash
poetry run python main.py                 # Rodar o script principal
poetry run python -m task_organizer.test_storage   # Rodar o script de teste com Poetry
python task_organizer/test_storage.py    # Rodar o script de teste sem Poetry
\`\`\`

---

## 💡 Comandos da CLI

\`\`\`bash
# Adicionar tarefa
poetry run python main.py add \"Comprar pão\" -d \"Ir na padaria\" -D 2025-06-10

# Listar tarefas pendentes (padrão)
poetry run python main.py list

# Listar tarefas concluídas
poetry run python main.py list --concluidas

# Marcar tarefa pendente como concluída (exemplo índice 1)
poetry run python main.py complete 1

# Listar todas as tarefas para referência de índices
poetry run python main.py list

# Remover tarefa pelo índice da lista completa (exemplo índice 2)
poetry run python main.py remove 2

# Limpar todas as tarefas
poetry run python main.py clear

# Listar apenas tarefas concluídas para obter índices
poetry run python main.py list --concluidas

# Remover tarefa concluída pelo índice da lista completa
poetry run python main.py remove <índice_da_lista_completa>
\`\`\`

---

## 📁 Estrutura de Pastas

\`\`\`
Gerenciamento-Python1/
├── main.py                  # Ponto de entrada do projeto
├── tasks.csv                # Arquivo com as tarefas salvas
├── test_storage.py          # Script de testes
├── task_organizer/
│   ├── cli.py               # CLI (em construção ou expansão futura)
│   ├── storage.py           # Funções de salvar/carregar tarefas
│   └── test_storage.py      # Versão interna de testes
├── pyproject.toml           # Configuração do projeto (Poetry)
├── poetry.lock              # Lockfile de dependências
├── README.md                # Este arquivo
└── LICENSE                  # Licença do projeto
\`\`\`

---

## 👥 Colaboradores

- João Teodorico de Sousa Segundo  
- Anderson Matheus Correia Souza de Assunção  
- Isabelly dos Santos Nascimento  

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT.
" > README.md
