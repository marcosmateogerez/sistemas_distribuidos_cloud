from src.core.observation import get_observations_by_project
from werkzeug.exceptions import BadRequest
from typing import List, Dict

def validate_observation_data(data):
    """
    Valida si se recibieron los datos "name" y "description".
    """
    if not data:
        raise BadRequest("No se enviaron datos")
    if "name" not in data or "description" not in data:
        raise BadRequest("Faltan campos obligatorios")
    return data["name"], data["description"]


def list_observations_by_project(project_id: int) -> List[Dict]:
    """
    Devuelve todas las observaciones de un proyecto, convertidas a diccionarios.
    """
    # Busca las observaciones en la base de datos.
    observations = get_observations_by_project(project_id=project_id)

    # Si no existen observaciones devuelve una lista vacía.
    if not observations:
        return []

    # Si existen, entonces convierte el resultado a lista de diccionarios y lo retorna.
    return [
        {
            "id": obs.id,
            "id_project": obs.id_project,
            "name": obs.name,
            "description": obs.description,
            "status": obs.status.value
        }
        for obs in observations
    ]