from src.core.user import services as user_functions 
from functools import wraps
from flask import request, jsonify, current_app, g
import jwt
from datetime import datetime, timezone

# def get_user():
#     """Devuelve el email del usuario registrado."""
#     return session.get("user")


# def get_is_super_user():
#     """Devuelve si el usuario actual es un super usuario."""
#     user_mail = session.get("user")
#     user_aux = user.get_user_by_email(user_mail)
#     return user_aux.is_super_user if user_aux else False


# def is_authenticated(session):
#     """Devuelve si el usuario está registrado."""
#     return session.get("user") is not None


# def login_required(func):
#     """
#     Decorador. Recibe un permiso y utiliza check_permission,
#     si es False genera abort 403.
#     """

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if not is_authenticated(session):
#             return abort(401)
#         return func(*args, **kwargs)

#     return wrapper


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        auth_header = request.headers.get("Authorization")
        
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            #Extraer token del header, si viene con Bearer  
            token = auth_header.split(" ")[1] if " " in auth_header else auth_header

        if not token:
            return jsonify({"error": "Token faltante"}), 401

        try:
            #Decodificar token
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])

            #Verificar expiración
            if "exp" in data and datetime.fromtimestamp(data["exp"], timezone.utc) < datetime.now(timezone.utc):
                return jsonify({"error": "Token expirado"}), 401

            #Obtener usuario
            user = user_functions.get_user_by_id(data["user_id"])
            if not user:
                return jsonify({"error": "Usuario no encontrado"}), 404

            #Guardar en contexto global de Flask
            g.current_user = user

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token invalido"}), 401

        return f(*args, **kwargs)

    return decorated

# def permission_check(permission):
#     """
#     Recibe un permiso y utiliza check_permission,
#     para verificar si el usuario actual lo tiene.
#     """
#     return check_permission(session, permission)


# def check(permission):
#     """
#     Decorador. Recibe un permiso y utiliza check_permission,
#     si es False genera abort 403.
#     """

#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if not check_permission(session, permission):
#                 return abort(403)
#             return func(*args, **kwargs)

#         return wrapper

#     return decorator


# def check_permission(session, permission):
#     """
#     Checkea si el usuario de la sesión tiene
#     el permiso ingresado o es un super usuario.
#     """
#     user_mail = session.get("user")
#     if not user_mail:
#         return False

#     user_aux = User.get_user_by_email(user_mail)
#     if user_aux is None:
#         return False

#     if user_aux.is_super_user:
#         return True

#     all_permissions = set()
#     for role in user_aux.roles:
#         all_permissions.update(auth.get_permissions(role))

#     return permission in all_permissions
