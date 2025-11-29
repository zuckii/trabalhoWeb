from flask import Flask, request

from .routes.home import home_bp
from .routes.auth import auth_bp
from .routes.movies import movies_bp
from db.database import DB_PATH, close_db

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "dev"
    app.config["DATABASE"] = DB_PATH
    
    app.teardown_appcontext(close_db)
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(movies_bp)
    

    # Make request available in all templates
    @app.context_processor
    def inject_request():
        return {'request': request}

    return app
