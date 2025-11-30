from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from db.database import get_all_movies, insert_review, get_rating_by_movie

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")

@movies_bp.route("/<int:id>")
def details_page(id):
    
    # A pagina details necessita de login.
    # Nem guest mode pode acessar a página details 
    if not session.get('user_id'):
        flash("Para avaliar é necessário realizar login.", "nok")
        return redirect(url_for('auth.login_page'))
    
    movies = get_all_movies()
    
    user_id = session["user_id"]
    
    movie = next((m for m in movies if m['id'] == id), None)

    if not movie:
        return "Filme não encontrado", 404
    
    reviews = get_rating_by_movie(movie['id'], user_id)

    return render_template("movies/details.html", movie=movie, reviews=reviews)


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