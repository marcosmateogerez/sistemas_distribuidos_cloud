from core.user import get_user_by_email, verify_user_password
from datetime import datetime, timedelta, timezone
from werkzeug.exceptions import BadRequest
from flask import current_app as app
import jwt

def validate_login_data(data):
    """
    Valida si se recibieron los datos "email" y "password" en el login.
    """
    if not data:
        raise BadRequest("No se enviaron datos")
    if "email" not in data or "password" not in data:
        raise BadRequest("Faltan campos obligatorios")
    return data["email"], data["password"]


def authenticate_user(email, password):
    """
    Devuelve el usuario autenticado si las credenciales son válidas, o none en caso contrario.
    """
    user = get_user_by_email(email)
    if not user or not verify_user_password(user, password):
        return None
    return user


def generate_jwt_token(user_id):
    """
    Genera un token JWT válido por 1 hora.
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")
    return token