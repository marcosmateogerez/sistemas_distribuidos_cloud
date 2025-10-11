from src.web.services.login import validate_login_data, authenticate_user, generate_jwt_token
from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

bp_login = Blueprint("login", __name__, url_prefix="/login")

@bp_login.post("/v1/authenticate")
def authenticate():
    """
    Autentica al usuario y genera un token JWT.
    """

    # Obtiene los datos del cuerpo JSON.
    data = request.get_json()
    try:
        email, password = validate_login_data(data)
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

    # Verifica si el usuario existe y si la contraseña es correcta.
    user = authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

    # Crea el token JWT.
    token = generate_jwt_token(user.id)

    # Devuelve el token JWT en formato JSON.
    return jsonify({"access_token": token}), 200