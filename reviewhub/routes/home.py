from flask import Blueprint, render_template, redirect, url_for, session
from db.database import get_all_movies

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def homepage():
    # If the user is not authenticated and guest mode is not enabled,
    # redirect to the login screen. Otherwise render the movies index.
    if not session.get('user_id') and not session.get('guest_mode'):
        return redirect(url_for('auth.login'))

    movies = get_all_movies()
    return render_template("home/index.html", movies=movies)

