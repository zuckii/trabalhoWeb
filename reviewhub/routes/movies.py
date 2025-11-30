from flask import Blueprint, render_template, redirect, url_for, session, flash
from db.database import get_all_movies

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")

@movies_bp.route("/<int:id>")
def details(id):
    
    # A pagina details necessita de login.
    # Nem guest mode pode acessar a página details 
    if not session.get('user_id'):
        flash("Para avaliar é necessário realizar login.", "nok")
        return redirect(url_for('auth.login_page'))
    
    movies = get_all_movies()

    movie = next((m for m in movies if m['id'] == id), None)

    if not movie:
        return "Filme não encontrado", 404
    
    return render_template("movies/details.html", movie=movie)