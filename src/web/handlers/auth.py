from flask import request, jsonify, current_app, g
from src.core import user as user_functions 
from datetime import datetime, timezone
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        auth_header = request.headers.get("Authorization")
        
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]

            # Extraer token del header, si viene con Bearer.
            token = auth_header.split(" ")[1] if " " in auth_header else auth_header

        if not token:
            return jsonify({"error": "Token faltante"}), 401

        try:
            # Decodificar token.
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])

            # Verificar expiración.
            if "exp" in data and datetime.fromtimestamp(data["exp"], timezone.utc) < datetime.now(timezone.utc):
                return jsonify({"error": "Token expirado"}), 401

            # Obtener usuario.
            user = user_functions.get_user_by_id(data["user_id"])
            if not user:
                return jsonify({"error": "Usuario no encontrado"}), 404

            # Guardar en contexto global de Flask.
            g.current_user = user

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token invalido"}), 401

        return f(*args, **kwargs)

    return decorated