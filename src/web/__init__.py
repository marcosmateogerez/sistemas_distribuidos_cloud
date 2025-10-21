from src.web.controllers.observation import bp_observation
from src.web.controllers.stage import bp as bp_stage
from src.web.controllers.login import bp_login
from src.core.database import db, reset
from src.docs.swagger_config import init_swagger
from src.core import seed_data
from flask import Flask, redirect
from src import config

# Creación de la app principal.
def create_app(env="production") -> Flask:
    app: Flask = Flask(__name__)

    # Seteo de configuración.
    app.config.from_object(config.config[env])
    db.init_app(app)

    # Comando para crear las tablas principales.
    @app.cli.command(name="seed-data")
    def seed_basic():
        seed_data.run()

    @app.cli.command(name="reset-db")
    def reset_db():
        reset(app)
        
    # Inicialización de Swagger.
    init_swagger(app)
    
    # Registro de blueprints.
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_stage)
    app.register_blueprint(bp_observation)
    
    # Renderización del home.
    @app.route("/")
    def home():
        return redirect("/apidocs")
    
    return app