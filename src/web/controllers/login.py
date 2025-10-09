from flask import Blueprint, render_template, request, jsonify
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from src.core.database import db
from src.core.user.model import User
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

    data = request.form
    email = data.get("email")
    password = data.get("password")

    # Buscar usuario
    user = User.query.filter_by(email=email).first()
    if not user:
        return render_template("login/login.html", error="Usuario no encontrado")

    # Verificar contraseña
    if not check_password_hash(user.password, password):
        return render_template("login/login.html", error="Contraseña incorrecta")

    # Crear JWT
    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.utcnow() + timedelta(hours=1)  # Expira en 1 hora
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    # Podés enviarlo como JSON, o guardarlo en cookie
    response = jsonify({"token": token})
    response.set_cookie("access_token", token, httponly=True)
    return render_template("layout.html")