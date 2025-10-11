from src.core.database import db
from src.core.role_permission.model import roles_permissions

class Permission(db.Model):
    """
    Modelo para representar un permiso.
    """
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    # Relación entre rol y permiso.
    roles = db.relationship("Role", secondary=roles_permissions, back_populates="permissions")