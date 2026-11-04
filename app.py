
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def conectar_banco():
    conexao = sqlite3.connect("database.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_banco():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            concluida INTEGER DEFAULT 0
        )
    """)

    conexao.commit()
    conexao.close()


@app.route("/")
def index():
    filtro = request.args.get("filtro", "todas")

    conexao = conectar_banco()

    # Estatísticas das tarefas
    total = conexao.execute(
        "SELECT COUNT(*) FROM tarefas"
    ).fetchone()[0]

    pendentes = conexao.execute(
        "SELECT COUNT(*) FROM tarefas WHERE concluida = 0"
    ).fetchone()[0]

    concluidas = conexao.execute(
        "SELECT COUNT(*) FROM tarefas WHERE concluida = 1"
    ).fetchone()[0]

    if total > 0:
        percentual = round((concluidas / total) * 100)
    else:
        percentual = 0

    # Filtros
    if filtro == "pendentes":
        tarefas = conexao.execute(
            "SELECT * FROM tarefas WHERE concluida = 0 ORDER BY id DESC"
        ).fetchall()

    elif filtro == "concluidas":
        tarefas = conexao.execute(
            "SELECT * FROM tarefas WHERE concluida = 1 ORDER BY id DESC"
        ).fetchall()

    else:
        filtro = "todas"
        tarefas = conexao.execute(
            "SELECT * FROM tarefas ORDER BY id DESC"
        ).fetchall()

    conexao.close()

    return render_template(
        "index.html",
        tarefas=tarefas,
        filtro=filtro,
        total=total,
        pendentes=pendentes,
        concluidas=concluidas,
        percentual=percentual
    )


# Adicionar tarefa
@app.route("/adicionar", methods=["POST"])
def adicionar():
    descricao = request.form["descricao"]

    if descricao.strip():
        conexao = conectar_banco()

        conexao.execute(
            "INSERT INTO tarefas (descricao, concluida) VALUES (?, ?)",
            (descricao, 0)
        )

        conexao.commit()
        conexao.close()

    return redirect("/")


# Editar tarefa
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    descricao = request.form["descricao"]

    if descricao.strip():
        conexao = conectar_banco()

        conexao.execute(
            "UPDATE tarefas SET descricao = ? WHERE id = ?",
            (descricao, id)
        )

        conexao.commit()
        conexao.close()

    return redirect("/")


# Excluir tarefa
@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    conexao = conectar_banco()

    conexao.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()

    return redirect("/")


# Concluir ou reabrir tarefa
@app.route("/concluir/<int:id>", methods=["POST"])
def concluir(id):
    conexao = conectar_banco()

    tarefa = conexao.execute(
        "SELECT concluida FROM tarefas WHERE id = ?",
        (id,)
    ).fetchone()

    if tarefa:
        novo_status = 0 if tarefa["concluida"] else 1

        conexao.execute(
            "UPDATE tarefas SET concluida = ? WHERE id = ?",
            (novo_status, id)
        )

        conexao.commit()

    conexao.close()

    return redirect("/")


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)
