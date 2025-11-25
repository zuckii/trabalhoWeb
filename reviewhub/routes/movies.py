from flask import Blueprint, render_template

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")

@movies_bp.route("/<int:id>")
def details(id):
    return render_template("movies/details.html", movie_id=id)

@movies_bp.route("/<int:id>/review")
def review(id):
    return render_template("movies/review.html", movie_id=id)
