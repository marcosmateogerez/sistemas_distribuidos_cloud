from flask import Blueprint, render_template, request, jsonify
from src.core.user.services import get_user_by_email, verify_user_password
import jwt
from datetime import datetime, timedelta
from flask import current_app as app

bp_login = Blueprint("login", __name__, url_prefix="/acceso")

@bp_login.get("/")
def login():
    """Retorna el HTML correspondiente para el formulario de inicio de sesión."""
    
    return render_template("login/login.html")


@bp_login.post("/")
def authenticate():
    """
    Valida los datos recibidos para confirmar el acceso al sitio o no, y genera el token JWT.
    """

    # Obtiene los datos del formulario.
    data = request.form
    email = data.get("email")
    password = data.get("password")

    # Verifica si el usuario existe y si la contraseña es correcta.
    user = get_user_by_email(email)
    if not user or not verify_user_password(user, password):
        return render_template("login/login.html", error="Usuario o contraseña incorrectos")

    # Creación del token JWT.
    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.utcnow() + timedelta(hours=1)
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    # Almacenamiento del token JWT en la cookie.
    response = jsonify({"token": token})
    response.set_cookie("access_token", token, httponly=True)
    return render_template("layout.html")