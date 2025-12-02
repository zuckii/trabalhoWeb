from reviewhub import create_app
from db.database import init_db

def run():
    app = create_app()

    print("Inicializando banco de dados...")
    init_db()
    
    app.run(debug=True, use_reloader=True)
