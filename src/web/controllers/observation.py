from src.web.services.observation import validate_observation_data
from src.web.handlers.permissions import requires_permission
from src.web.handlers.auth import token_required
from src.core.observation import create_observation
from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from flask import g

bp = Blueprint("observation", __name__, url_prefix="/observations")

@bp.post("/v1/add_observation/<int:project_id>")
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