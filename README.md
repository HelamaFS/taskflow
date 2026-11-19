# TaskFlow

**Sistema web de gerenciamento de tarefas — projeto acadêmico.**

O **TaskFlow** é uma aplicação web para cadastrar, organizar e acompanhar tarefas, com controle de prazos, calendário, indicadores de progresso e personalização de aparência. O sistema possui autenticação de usuários e mantém as tarefas vinculadas à conta de cada pessoa.

## Funcionalidades

### Gerenciamento de tarefas
- Adicionar, visualizar e excluir tarefas.
- Editar a descrição e a data de entrega das tarefas pendentes.
- Marcar tarefas como concluídas e reabri-las.
- Impedir a edição de tarefas concluídas até que sejam reabertas.
- Filtrar a lista por **Todas**, **Pendentes** e **Concluídas**.

### Dashboard
- Exibir o total de tarefas, a quantidade de pendentes e de concluídas.
- Mostrar o percentual de conclusão e uma barra visual de progresso.

### Usuários e personalização
- Cadastrar usuários e realizar login/logout.
- Manter as tarefas separadas por usuário.
- Alterar o tema (claro ou escuro) e a cor de destaque da interface.

### Calendário e prazos
- Definir datas de entrega para tarefas.
- Visualizar tarefas organizadas por dia em um calendário mensal.
- Navegar entre os meses.

### Publicação
- Aplicação publicada na **Vercel**, com banco **PostgreSQL hospedado na Neon**.
- Favicon personalizado do TaskFlow.

## Evolução por avaliação

| Etapa | Funcionalidades desenvolvidas |
|---|---|
| **AC1** | Cadastro e listagem de tarefas; estrutura inicial com Flask e SQLite. |
| **AC2** | Edição de tarefas. |
| **AC3** | Conclusão/reabertura, filtros e dashboard de estatísticas. |
| **AC4 (final)** | Cadastro/login de usuários, aparência personalizada, calendário e prazos, regras de edição e publicação online com PostgreSQL. |

## Tecnologias utilizadas

- **Front-end:** HTML e CSS (templates com Jinja2).
- **Back-end:** Python e Flask.
- **Banco de dados local:** SQLite.
- **Banco de dados online:** PostgreSQL (Neon).
- **Hospedagem:** Vercel.
- **Versionamento:** Git e GitHub.

## Estrutura do projeto

```text
taskflow/
├── app.py
├── requirements.txt
├── vercel.json
├── .gitignore
├── static/
│   ├── style.css
│   └── favicon.ico
└── templates/
    ├── index.html
    ├── login.html
    ├── cadastro.html
    └── calendario.html
```

> O arquivo `database.db` é usado apenas no desenvolvimento local e não deve ser incluído no repositório Git.

## Como executar localmente

**Pré-requisito:** Python instalado.

1. Clone o repositório:

   ```bash
   git clone https://github.com/HelamaFS/taskflow.git
   cd taskflow
   ```

2. Instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Execute a aplicação:

   ```bash
   python app.py
   ```

4. Abra **http://127.0.0.1:5000** no navegador.

Sem a variável `DATABASE_URL`, a aplicação utiliza o banco local **SQLite**. Para conectar ao Neon, configure `DATABASE_URL` com a string PostgreSQL e `SECRET_KEY` com uma chave aleatória forte. **Nunca publique essas variáveis, senhas ou arquivos `.env` no GitHub.**

## Arquitetura

O TaskFlow está organizado em três camadas:

1. **Apresentação:** páginas HTML, CSS e formulários de interação.
2. **Aplicação:** rotas, autenticação e regras de negócio implementadas com Flask.
3. **Persistência:** SQLite no ambiente local e PostgreSQL/Neon na versão publicada.

## Acesso e repositório

- **Site online:** adicione aqui o endereço definitivo do seu projeto no Vercel.
- **Código-fonte:** https://github.com/HelamaFS/taskflow

## Objetivo do projeto

Desenvolver um sistema web funcional, aplicando conhecimentos de front-end, back-end, integração com banco de dados, autenticação de usuários, versionamento e publicação de aplicações web.

**Projeto acadêmico — TaskFlow.**
