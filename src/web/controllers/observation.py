from src.web.services.observation import validate_observation_data, list_observations_by_project
from src.web.handlers.permissions import requires_permission
from src.web.handlers.auth import token_required
from src.core.observation import create_observation
from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from flask import g

bp_observation = Blueprint("observation", __name__, url_prefix="/observations")

@bp_observation.post("/v1/add_observation/<int:project_id>")
@token_required
@requires_permission("add_observation")
def add_observation(project_id: int):
    """
    Endpoint para agregar una observación a un proyecto a partir de su ID de proyecto.
    """
    # Obtiene los datos del cuerpo JSON.
    data = request.get_json()
    try:
        name, description = validate_observation_data(data)
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

    # Crea la observación y la almacena en la base de datos.
    create_observation(
        project_id=project_id,
        name=name,
        description=description
    )

    return jsonify({"message": f"Observación '{name}' agregada correctamente al proyecto {project_id}"}), 201


@bp_observation.get("/v1/list_observations/<int:project_id>")
@token_required
@requires_permission("list_observations")
def get_observations(project_id: int):
    """
    Endpoint para obtener todas las observaciones de un proyecto según su ID.
    """
    observations = list_observations_by_project(project_id)

    if not observations:
        return jsonify({"message": f"No se encontraron observaciones para el proyecto con ID {project_id}."}), 404

    return jsonify(observations), 200