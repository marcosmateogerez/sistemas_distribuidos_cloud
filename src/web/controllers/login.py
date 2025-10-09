from flask import Blueprint, render_template

bp_login = Blueprint("login", __name__, url_prefix="/acceso")

@bp_login.get("/")
def login():
    """Retorna el HTML correspondiente para el formulario de inicio de sesión."""
    
    return render_template("login/login.html")