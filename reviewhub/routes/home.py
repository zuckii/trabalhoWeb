from flask import Blueprint, render_template, redirect, url_for, session
from db.database import get_all_movies

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def homepage():
    
    movies = get_all_movies()
    return render_template("home/index.html", movies=movies)

