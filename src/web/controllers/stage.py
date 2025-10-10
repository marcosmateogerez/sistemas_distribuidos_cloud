from flask import Blueprint, request, jsonify
from src.core.stage.model import Stage, CoverageRequest
from src.core import stage as stage_functions



bp = Blueprint("stage", __name__, url_prefix="/stages")

@bp.get("v1/get_available_stages/<int:project_id>")
def get_available_stages(project_id: int):
    """
    Endpoint para obtener las etapas disponibles de un proyecto.
    """
  
    stages_list = stage_functions.get_available_stages(project_id)
    print(stages_list)
    return stages_list, 200

