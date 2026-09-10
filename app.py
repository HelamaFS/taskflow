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
            descricao TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


@app.route("/")
def index():
    conexao = conectar_banco()

    tarefas = conexao.execute(
        "SELECT * FROM tarefas ORDER BY id DESC"
    ).fetchall()

    conexao.close()

    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    descricao = request.form["descricao"]

    if descricao.strip():
        conexao = conectar_banco()

        conexao.execute(
            "INSERT INTO tarefas (descricao) VALUES (?)",
            (descricao,)
        )

        conexao.commit()
        conexao.close()

    return redirect("/")


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)