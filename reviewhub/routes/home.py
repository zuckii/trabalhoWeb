from flask import Blueprint, render_template, session, request
from db.database import get_all_movies, get_movies_by_genre, get_all_genres

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def homepage():
    genero = request.args.get("genero")
    generos = get_all_genres()

    if genero:
        movies = get_movies_by_genre(genero)
    else:
        movies = get_all_movies()
    return render_template("home/index.html", movies=movies, generos=generos, selected_genero=genero)
