from flask import Flask
from src import config
from src.core.database import db, reset
from src.core.user.model import User
from src.core.role.model import Role
from src.core.permission.model import Permission
from src.core.role_permission.model import role_permission

# Creación de la app principal.
def create_app(env="development") -> Flask:
    app: Flask = Flask(__name__)

    # Seteo de configuración.
    app.config.from_object(config.config[env])
    db.init_app(app)
    reset(app)

    # Renderización del home.
    @app.route("/")
    def home():
        return "Backend ejecutando correctamente ✅."
    
    return app