from src.core.user import get_user_by_id
from flask import g, jsonify
from functools import wraps

def requires_permission(permission_name: str):
    """
    Decorador que valida que el usuario tenga un permiso específico.
    """
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user = getattr(g, "current_user", None)
            if not user:
                return jsonify({"error": "Usuario no autenticado"}), 401
            
            role_permissions = [p.name for p in user.role.permissions]
            if permission_name not in role_permissions:
                return jsonify({"error": "Permiso denegado"}), 403

            return f(*args, **kwargs)
        return decorated
    return decorator