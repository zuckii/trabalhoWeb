from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev"

    from .routes.home import home_bp
    from .routes.auth import auth_bp
    from .routes.movies import movies_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(movies_bp)

    return app
