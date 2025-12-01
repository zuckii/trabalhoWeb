import json
import sqlite3
import os
from flask import current_app, g
from reviewhub.utils.security import hash_senha

DB_PATH = os.path.join(os.path.dirname(__file__), "reviewhub.db")
BASE_DIR = os.path.dirname(__file__)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Executa o schema.sql
    with open(os.path.join(BASE_DIR, "schema.sql"), "r", encoding="utf8") as f:
        cur.executescript(f.read())

    # Adiciona os generos na tabela do banco
    with open(os.path.join(BASE_DIR, "generos.json"), "r", encoding="utf8") as f:
        generos = json.load(f)

    print("Adicionando generos")
    for genero in generos:    
        cur.execute(
            """INSERT OR IGNORE INTO Genero (nome) VALUES (?)""",
            (genero["nome"],)
        )
        
    # Adiciona os filmes
    print("Adicionando filmes")
    with open(os.path.join(BASE_DIR, "filmes.json"), "r", encoding="utf8") as f:
        filmes = json.load(f)

    for filme in filmes:

        # Pegar id do genero
        cur.execute("SELECT id FROM Genero WHERE nome = ?", (filme["genero"],))
        genero_id = cur.fetchone()

        if genero_id:
            cur.execute("""
                INSERT OR IGNORE INTO Filmes (nome, genero_id, imagem)
                VALUES (?, ?, ?)
            """, (filme["nome"], genero_id[0], filme["imagem"]))

        else:
            raise Exception(
                f"Nenhum id de genero encontrado para o filme '{filme['nome']}', genero '{filme['genero']}'"
            )

    cur.execute("SELECT id FROM Usuario WHERE username = ?", ("admin",))
    admin_exists = cur.fetchone()

    # Verificando se já existe usuario padrão
    if not admin_exists:
        senha = hash_senha("admin")
        print("Criando admin padrão")
        cur.execute("""INSERT INTO Usuario (nome, username, senha) VALUES (?, ?, ?)""",
                    ("admin", "admin", senha))
    else:
        print("Admin já existe")

    conn.commit()
    conn.close()


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def get_all_movies():
    db = get_db()
    return db.execute("SELECT * FROM Filmes").fetchall()


def get_movie_by_id(fid):
    db = get_db()
    return db.execute(
        "SELECT * FROM Filmes WHERE id = ?",
        (fid,)
    ).fetchone()

def get_user_by_username(username):
    db = get_db()
    return db.execute("SELECT * FROM Usuario WHERE username = ?", 
                      (username,)
                      ).fetchone()


def get_userId_by_username(username):
    db = get_db()
    return db.execute("SELECT id FROM Usuario WHERE username = ?", 
                      (username,)
                      ).fetchone()

def insert_user(nome, username, senha):
    db = get_db()
    db.execute(
            "INSERT INTO Usuario (nome, username, senha) VALUES (?, ?, ?)",
            (nome, username, senha)
        )
    db.commit()
    

def get_movies_by_genre(genero):
    conn = get_db()
    genero_id = conn.execute("SELECT id FROM Genero WHERE nome = ?", (genero,)).fetchone()
    cursor = conn.execute("SELECT * FROM Filmes WHERE genero_id = ?", (genero_id[0],))
    movies = cursor.fetchall()

    return [dict(row) for row in movies]


def get_all_genres():
    db = get_db()
    return db.execute("SELECT * FROM Genero ORDER BY nome ASC").fetchall()


def insert_review(usuario_id, filme_id, nota, comentario):
    db = get_db()
    db.execute("""
        INSERT OR REPLACE INTO Avaliacao (usuario_id, filme_id, nota, comentario)
        VALUES (?, ?, ?, ?)
    """, (usuario_id, filme_id, nota, comentario))
    db.commit()


# Lista o nome, nota de todas as avaliações dos usuarios, menos a do usuario proprio
def get_rating_by_movie(filme_id, user_id):
    db = get_db()
    query = db.execute("""
    
    SELECT 
    u.username AS usuario,
    a.nota,
    a.comentario
    FROM Avaliacao a
    JOIN Usuario u ON u.id = a.usuario_id
    WHERE a.filme_id = ?
    AND a.usuario_id != ?;
    """, (filme_id, user_id)).fetchall()


    return [dict(row) for row in query]

def get_movie_rating_average(filme_id):
    db = get_db()
    query = db.execute("""
        SELECT AVG(nota) AS media
        FROM Avaliacao
        WHERE filme_id = ?
    """, (filme_id,)).fetchone()

    return query["media"] if query["media"] is not None else 0


def update_review(usuario_id, filme_id, nota, comentario):
    db = get_db()
    db.execute("""
        UPDATE Avaliacao
        SET nota = ?, comentario = ?
        WHERE usuario_id = ? AND filme_id = ?
    """, (nota, comentario, usuario_id, filme_id))
    db.commit()

def get_reviews_by_user(usuario_id):
    db = get_db()
    return db.execute("""
        SELECT
            a.nota
            , a.comentario
            , f.nome as filme_nome
            , f.imagem as filme_imagem
            , f.id as filme_id
        FROM Avaliacao a inner join Filmes f on a.filme_id = f.id WHERE usuario_id = ?
    """, (usuario_id,)).fetchall()


def delete_review(usuario_id, filme_id):
    db = get_db()
    db.execute("""
        DELETE FROM Avaliacao WHERE usuario_id = ? AND filme_id = ?
    """, (usuario_id, filme_id))
    db.commit()
