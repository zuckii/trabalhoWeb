from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from db.database import get_user_by_username, get_userId_by_username, insert_user
from reviewhub.utils.security import *

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login")
def login_page():
    return render_template("auth/login.html")


@auth_bp.post("/login")
def login():
    username = request.form.get("username")
    senha = request.form.get("password")
    user = get_user_by_username(username)

    if not username or not senha:
        flash("Preencha todos os campos.", "nok")
        return redirect(url_for("auth.login_page"))
    
    if user is None:
        flash("Usuário não encontrado.", "nok")
        return redirect(url_for("auth.login_page"))

    if not verifica_senha(user["senha"], senha):
        flash("Senha incorreta.", "nok")
        return redirect(url_for("auth.login_page"))

    session["user_id"] = user["id"]
    session["user_nome"] = user["nome"]
    session["username"] = user["username"]

    return redirect(url_for("home.homepage"))


@auth_bp.route("/register")
def register_page():
    return render_template("auth/register.html")


@auth_bp.post("/register")
def register():
    nome = request.form.get("name")
    username = request.form.get("username")
    senha = request.form.get("password")

    if not nome or not username or not senha:
        flash("Preencha todos os campos.", "nok")
        return redirect(url_for("auth.register_page"))

    existe = get_userId_by_username(username)

    if existe:
        flash("Já existe um usuário com esse username.", "nok")
        return redirect(url_for("auth.register_page"))

    senha = hash_senha(senha)
    insert_user(nome, username, senha)

    flash("Cadastro realizado com sucesso! Faça login.", "ok")
    return redirect(url_for("auth.login_page"))



@auth_bp.route("/guest")
def guest_login():
    session['guest_mode'] = True
    return redirect(url_for("home.homepage"))


@auth_bp.route("/logout")
def logout():
    # clear user session and redirect to login
    session.pop("user_id", None)
    session.pop("user_nome", None)
    session.pop("username", None)
    session.pop("guest_mode", None)
    return redirect(url_for("auth.login_page"))
