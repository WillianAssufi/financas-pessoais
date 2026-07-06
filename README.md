# 💰 Finanças Pessoais API

API REST para controle de finanças pessoais, desenvolvida com Python, FastAPI e PostgreSQL.

> ⚠️ Projeto em desenvolvimento — novas funcionalidades sendo adicionadas gradualmente.

## 🚀 Tecnologias

- **Python 3.14** — linguagem principal
- **FastAPI** — framework web para criação da API
- **PostgreSQL** — banco de dados relacional
- **SQLAlchemy 2.0** — ORM assíncrono
- **Alembic** — migrations do banco de dados
- **Pydantic** — validação de dados
- **JWT (python-jose)** — autenticação
- **bcrypt** — hash de senhas
- **pytest + httpx** — testes automatizados
- **uv** — gerenciador de pacotes

## ⚙️ Como rodar localmente

### Pré-requisitos

- Python 3.12+
- PostgreSQL instalado e rodando
- uv instalado (`pip install uv`)

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/WillianAssufi/financas-pessoais.git
cd financas-pessoais/backend
```

**2. Crie o ambiente virtual e instale as dependências**
```bash
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
uv sync
```

**3. Configure as variáveis de ambiente**
```bash
cp .env.example .env
```
Edite o `.env` com suas configurações (senha do banco, secret key, etc).

**4. Crie os bancos de dados**
```sql
CREATE DATABASE financas_pessoais;
CREATE DATABASE financas_pessoais_test;
```

**5. Rode as migrations**
```bash
alembic upgrade head
```

**6. Inicie o servidor**
```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://localhost:8000`.
Documentação Swagger em `http://localhost:8000/docs`.

## 🔑 Variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`:

| Variável | Descrição |
|---|---|
| `DATABASE_URL` | URL de conexão com o banco de dados principal |
| `TEST_DATABASE_URL` | URL de conexão com o banco de dados de testes |
| `SECRET_KEY` | Chave secreta para assinar os tokens JWT |

## 🧪 Rodando os testes

```bash
pytest tests/ -v
```

## 📁 Estrutura do projeto

```
backend/
├── app/
│   ├── main.py           # ponto de entrada da aplicação
│   ├── database.py       # configuração do banco de dados
│   ├── models.py         # modelos do banco de dados (SQLAlchemy)
│   ├── schemas.py        # schemas de validação (Pydantic)
│   ├── security.py       # hash de senha e JWT
│   ├── dependencies.py   # dependências compartilhadas (autenticação)
│   └── routers/
│       ├── auth.py       # rota de login
│       ├── usuarios.py   # CRUD de usuários
│       ├── categorias.py # CRUD de categorias
│       └── transacoes.py # CRUD de transações
├── migrations/           # migrations do Alembic
├── tests/
│   ├── conftest.py       # configuração dos testes
│   ├── test_auth.py      # testes de autenticação
│   ├── test_usuarios.py  # testes de usuários
│   └── test_transacoes.py# testes de transações
├── .env.example          # exemplo de variáveis de ambiente
├── alembic.ini           # configuração do Alembic
├── pytest.ini            # configuração do pytest
└── pyproject.toml        # dependências do projeto
```

## 📌 Endpoints principais

| Método | Rota | Descrição | Auth |
|---|---|---|---|
| POST | `/usuarios/` | Criar usuário | Não |
| GET | `/usuarios/` | Listar usuários | Não |
| PUT | `/usuarios/{id}` | Atualizar usuário | Não |
| DELETE | `/usuarios/{id}` | Deletar usuário | Não |
| POST | `/login` | Fazer login | Não |
| GET | `/categorias/` | Listar categorias | Sim |
| POST | `/categorias/` | Criar categoria | Sim |
| PUT | `/categorias/{id}` | Atualizar categoria | Sim |
| DELETE | `/categorias/{id}` | Deletar categoria | Sim |
| GET | `/transacoes/` | Listar transações | Sim |
| POST | `/transacoes/` | Criar transação | Sim |
| PUT | `/transacoes/{id}` | Atualizar transação | Sim |
| DELETE | `/transacoes/{id}` | Deletar transação | Sim |

## 📖 Documentação

Com o servidor rodando, acesse:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🚧 Roadmap

- [x] API REST com FastAPI
- [x] Autenticação com JWT
- [x] CRUD de usuários, categorias e transações
- [x] Testes automatizados com pytest
- [ ] Frontend em React
- [ ] Dashboard com resumo financeiro
- [ ] Gráficos de gastos por categoria
- [ ] Filtros por data e categoria
- [ ] Relatórios mensais
- [ ] Deploy