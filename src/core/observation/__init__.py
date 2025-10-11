from src.core.observation.model import Observation, Status
from src.core.database import db
from typing import List, Optional

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


def mark_observation_as_resolved(observation_id: int) -> Optional[Observation]:
    """
    Marca una observación como RESOLVED a partir de su ID.
    """
    observation = Observation.query.get(observation_id)
    if observation:
        observation.status = Status.RESOLVED
        db.session.commit()
        return observation
    return None