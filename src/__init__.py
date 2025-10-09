from flask import Flask
from src import config

# Creación de la app principal.
def create_app(env="development") -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(config.config[env])

    # Renderización del home.
    @app.route("/")
    def home():
        return "Backend ejecutando correctamente ✅."
    
    return app