# ✅ Task Organizer – Gerenciador de Tarefas em Python

Este projeto é um gerenciador de tarefas simples, desenvolvido em Python. Ele permite **salvar** e **carregar tarefas** a partir de um arquivo CSV, simulando um sistema básico de controle de atividades pessoais.

---

## ✨ Funcionalidades

- ➕ Adicionar tarefas manualmente (via código ou script)
- 💾 Salvar tarefas em um arquivo `tasks.csv`
- 📂 Carregar tarefas salvas e exibir no terminal

---

## 🗃️ Armazenamento

- Utiliza arquivos CSV como forma simples de persistência de dados
- Organização modular com separação de responsabilidades (`storage`, `test_storage`, `main`)

---

## 🔧 Tecnologias e Dependências

- **Python 3.10+ até 3.13**
- **Poetry** como gerenciador de dependências
- Bibliotecas padrão: `csv`, `pathlib`

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Instale o ambiente com o Poetry:

```bash
poetry install
```

---

## ▶️ Como executar

### Rodar o script principal:

```bash
poetry run python main.py
```

### Rodar o script de teste:

```bash
poetry run python -m task_organizer.test_storage
```

Ou sem o Poetry:

```bash
python task_organizer/test_storage.py
```

---

## 📁 Estrutura de Pastas

```
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
```

---

## 👥 Colaboradores

- João Teodorico de Sousa Segundo  
- Anderson Matheus Correia Souza de Assunção  
- Isabelly dos Santos Nascimento

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT.
