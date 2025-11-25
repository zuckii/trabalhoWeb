from flask import Blueprint, render_template, session, redirect, url_for

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")


@auth_bp.route("/register")
def register():
    return render_template("auth/register.html")


@auth_bp.route("/logout")
def logout():
    # clear user session and redirect to homepage
    session.pop("user_id", None)
    return redirect(url_for("home.homepage"))
