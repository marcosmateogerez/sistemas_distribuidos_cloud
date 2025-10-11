from src.core.database import db
from src.core.role_permission.model import role_permission

class Role(db.Model):
    """
    Modelo para representar un rol.
    """
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    # Relación entre usuario y rol.
    user = db.relationship("User", back_populates="role")

    # Relación entre rol y permiso.
    permissions = db.relationship("Permission", secondary=role_permission, back_populates="roles")