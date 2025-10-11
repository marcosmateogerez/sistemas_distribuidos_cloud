from flask import jsonify
from src.core import stage as stage_functions
from src.core.stage.model import status as status_stage
from src.core.stage.model import Stage
from src.core.stage.model import CoverageRequest
from src.core.database import db


def get_available_stages(project_id: int):
    """
    funcion para obtener las etapas disponibles de un proyecto.
    """
    stages_list = stage_functions.get_available_stages(project_id)
    
    # Convertir los objetos Stage a diccionarios
    stages_dict = [stage.to_dict() for stage in stages_list]

    # Retornar la lista de etapas como JSON
    return stages_dict
    
    
def cover_stage(stage_id: int):
    """
    funcion para cubrir una etapa específica según su ID.
    """
    stage = stage_functions.cover_stage(stage_id)
    # Lógica para indicar que la etapa ya está cubierta
    if stage:
        if stage.status == status_stage.PENDING:
            stage_functions.set_stage_in_progress(stage_id)
            return True
    return False



def finish_stage(stage_id: int):
    """
    funcion para finalizar una etapa específica según su ID.
    """
    stage = stage_functions.cover_stage(stage_id)
    # Lógica para indicar que la etapa ya está cubierta
    if stage:
        if stage.status == status_stage.IN_PROGRESS:
            stage_functions.set_stage_as_finished(stage_id)
            return True
    return False


def create_stage(data: dict):
    """
    funcion para crear una nueva etapa.
    """
    coverage_request = CoverageRequest[data["coverage_request"]]

    new_stage = Stage(
        id_project=data["id_project"],
        name=data["name"],
        description=data.get("description"),
        start_date=data["start_date"],
        end_date=data.get("end_date"),
        coverage_request=coverage_request
    )
    stage_functions.create_stage(new_stage)
    if new_stage:
        return new_stage
    return None
    
        