from src.core.database import db
from sqlalchemy import Enum
import enum

class CoverageRequest(enum.Enum):
    """
    Enum para los pedidos de cobertura de un proyecto.
    """
    DINERO = "DINERO"
    MATERIALES = "MATERIALES"
    MANO_DE_OBRA = "MANO_DE_OBRA"


class Stage(db.Model):
    """
    Modelo para representar la etapa de un proyecto.
    """
    __tablename__ = "stages"
    id = db.Column(db.Integer, primary_key=True)
    id_project = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    coverage_request = db.Column(Enum(CoverageRequest), nullable=False)
    