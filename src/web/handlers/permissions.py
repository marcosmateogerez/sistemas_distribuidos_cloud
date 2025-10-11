from src.core.user import get_user_by_id
from flask import g, jsonify
from functools import wraps

def requires_permission(permission: str):
    """
    Decorador que valida que el usuario tenga un permiso específico.
    """
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user_id = getattr(g, "user_id", None)
            if not user_id:
                return jsonify({"error": "Usuario no autenticado"}), 401

            user = get_user_by_id(user_id)
            if not user:
                return jsonify({"error": "Usuario no encontrado"}), 404

            if permission not in user.permissions:
                return jsonify({"error": "Permiso denegado"}), 403

            return f(user=user, *args, **kwargs)
        return decorated
    return decorator