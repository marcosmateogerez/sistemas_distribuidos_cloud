from src.core.observation.model import Observation, Status
from src.core.database import db
from typing import List

def create_observation(project_id: int, name: str, description: str = "") -> Observation:
    """
    Crea una nueva observación para un proyecto y la guarda en la base de datos.
    """
    observation = Observation(
        id_project=project_id,
        name=name,
        description=description,
        status=Status.PENDING
    )
    db.session.add(observation)
    db.session.commit()
    return observation


def get_observations_by_project(project_id: int) -> List[Observation]:
    """
    Devuelve todas las observaciones asociadas a un proyecto.
    """
    return Observation.query.filter_by(id_project=project_id).all()