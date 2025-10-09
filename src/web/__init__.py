from flask import Flask, render_template
from src import config
from src.core.database import db, reset
from src.core import seed_data
from src.web.controllers.login import bp_login

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

    # Registro de blueprints.
    app.register_blueprint(bp_login)

    # Renderización del home.
    @app.route("/")
    def home():
        return render_template("layout.html")
    
    return app