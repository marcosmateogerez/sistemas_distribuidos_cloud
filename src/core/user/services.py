from werkzeug.security import check_password_hash
from src.core.user.model import User

def get_user_by_id(user_id: int) -> User | None:
    """
    Devuelve un usuario por su ID o none si no existe.
    """
    if not user_id:
        return None
    return User.query.get(user_id)


def get_user_by_email(email: str) -> User | None:
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

def get_user_by_id(user_id: int):
    """
    Devuelve un usuario por ID o devuelve none si no existe.
    """
    return User.query.get(user_id)