from flask import Flask

# Creación de la app principal.
def create_app() -> Flask:
    app: Flask = Flask(__name__)

    # Renderización del home.
    @app.route("/")
    def home():
        return "Backend ejecutando correctamente ✅."
    
    return app