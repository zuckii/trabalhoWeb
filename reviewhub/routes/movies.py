from flask import Blueprint, render_template, redirect, url_for, session
from db.database import get_all_movies

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")

@movies_bp.route("/<int:id>")
def details(id):
    
    if not session.get('user_id') and not session.get('guest_mode'):
        return redirect(url_for('auth.login'))

    movies = get_all_movies()

    movie = next((m for m in movies if m['id'] == id), None)

    if not movie:
        return "Filme não encontrado", 404
    
    return render_template("movies/details.html", movie=movie)
