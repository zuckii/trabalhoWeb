from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from db.database import get_all_movies, get_reviews_by_user, insert_review, delete_review, update_review

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")

@movies_bp.route("/<int:id>")
def details_page(id):
    
    # A pagina details necessita de login.
    # Nem guest mode pode acessar a página details 
    if not session.get('user_id'):
        flash("Para avaliar é necessário realizar login.", "nok")
        return redirect(url_for('auth.login_page'))
    
    movies = get_all_movies()

    movie = next((m for m in movies if m['id'] == id), None)

    review = next((r for r in get_reviews_by_user(session.get('user_id')) if r['filme_id'] == id), None)

    if not movie:
        return "Filme não encontrado", 404
    
    return render_template("movies/details.html", movie=movie, review=review)


@movies_bp.route("/mine")
def mine_reviews_page():
    
    # A pagina de listagem de avaliações necessita de login.
    if not session.get('user_id'):
        flash("Para listar suas avaliações é necessário realizar login.", "nok")
        return redirect(url_for('auth.login_page'))
    
    reviews = get_reviews_by_user(session.get('user_id'))
    
    return render_template("movies/mine.html", reviews=reviews)

@movies_bp.delete("/<int:id>")
def remove_review(id):
    
    # Para remover avaliações é necessário realizar login.
    if not session.get('user_id'):
        flash("Para remover avaliações é necessário realizar login.", "nok")
        return redirect(url_for('auth.login_page'))
    
    reviews = get_reviews_by_user(session.get('user_id'))
    review = next((r for r in reviews if r['filme_id'] == id), None)
    if review:
        delete_review(session.get('user_id'), id)
        flash("Avaliação removida com sucesso!", "ok")
    else:
        flash("Avaliação não encontrada.", "nok")
    
    # reviews = get_reviews_by_user(session.get('user_id'))
    return redirect(url_for("movies.mine_reviews_page"))



@movies_bp.post("/<int:id>")
def details(id):
    user_id = session["user_id"]
    nota = float(request.form.get("rating"))
    comentario = request.form.get("review")

    if nota < 0 or nota > 5:
        flash("Nota inválida. Deve ser entre 0 e 5.", "nok")
        return redirect(url_for("movies.details_page", id=id))

    try:
        insert_review(user_id, id, nota, comentario)
        flash("Avaliação enviada com sucesso!", "ok")
    except Exception as e:
        flash(f"Erro ao salvar avaliação: {e}", "nok")
        return redirect(url_for("movies.details_page", id=id))

    return redirect(url_for("home.homepage"))


@movies_bp.post("/update/<int:id>")
def update_review_route(id):
    user_id = session.get("user_id")
    
    if not user_id:
        flash("Para atualizar avaliações é necessário realizar login.", "nok")
        return redirect(url_for('auth.login_page'))
    
    nota = float(request.form.get("rating"))
    comentario = request.form.get("review")

    if nota < 0 or nota > 5:
        flash("Nota inválida. Deve ser entre 0 e 5.", "nok")
        return redirect(url_for("movies.details_page", id=id))

    try:
        update_review(user_id, id, nota, comentario)
        flash("Avaliação atualizada com sucesso!", "ok")
    except Exception as e:
        flash(f"Erro ao atualizar avaliação: {e}", "nok")
        return redirect(url_for("movies.details_page", id=id))

    return redirect(url_for("home.homepage"))
