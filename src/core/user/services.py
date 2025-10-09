from src.core.user.model import User
from werkzeug.security import check_password_hash

def get_user_by_email(email: str):
    """
    Devuelve un usuario por email o devuelve none si no existe.
    """
    return User.query.filter_by(email=email).first()


def verify_user_password(user: User, password: str) -> bool:
    """
    Valida si la contraseña recibida por parámetro coincide con la del usuario.
    """
    if not user:
        return False
    return check_password_hash(user.password, password)