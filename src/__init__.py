from flask import Flask
from src import config
from src.core.database import db, reset
from src.core import seed_data
from src.core.user.model import User

# Creación de la app principal.
def create_app(env="development") -> Flask:
    app: Flask = Flask(__name__)

    # Seteo de configuración.
    app.config.from_object(config.config[env])
    db.init_app(app)
    reset(app)

    # Comando para crear las tablas principales.
    @app.cli.command(name="seed-data")
    def seed_basic():
        seed_data.run()

    # Renderización del home.
    @app.route("/")
    def home():
        return "Backend ejecutando correctamente ✅."
    
    return app