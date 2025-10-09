from src.core.database import db

class User(db.Model):
    """
    Modelo para representar un usuario.
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=True)

    # Clave foránea para acceder al rol.
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)

    # Relación entre usuario y rol.
    role = db.relationship("Role", back_populates="user")