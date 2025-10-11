from flask import Blueprint, request, jsonify
from src.core.stage.model import Stage, CoverageRequest
from src.web.services import stage as stage_service 



bp = Blueprint("stage", __name__, url_prefix="/stages")

@bp.get("v1/get_available_stages/<int:project_id>")
def get_available_stages(project_id: int):
    """
    Endpoint para obtener las etapas disponibles de un proyecto.
    """
    stages_list = stage_service.get_available_stages(project_id)
    if not stages_list:
        return jsonify({"message": "No se encontraron etapas para el proyecto especificado."}), 404
    
    return jsonify(stages_list), 200


@bp.get("v1/cover_stage/<int:stage_id>")
def cover_stage_by_id(stage_id: int):
    """
    Endpoint para cubrir una etapa específica según su ID.
    """
    # Aquí iría la lógica para cubrir la etapa con el ID proporcionado
    result = stage_service.cover_stage(stage_id)
    if result:
        return jsonify({"message": f"La etapa con ID {stage_id} ha pasado de pendiente a en ejecucion exitosamente."}), 200
    return jsonify({"message": f"No se pudo cubrir la etapa con ID {stage_id}. Es posible que ya este en progreso o haya sido cubierta."}), 400


@bp.get("v1/finish_stage/<int:stage_id>")
def finish_stage_by_id(stage_id: int):
    """
    Endpoint para finalizar una etapa especifica según su ID.
    """
    result = stage_service.finish_stage(stage_id)
    if result: 
        return jsonify({"message": f"La etapa con ID {stage_id} ha sido finalizada exitosamente."}), 200
    return jsonify({"message": f"No se pudo finalizar la etapa con ID {stage_id}. Es posible que no este pendiente o que ya haya finalizado."}), 400