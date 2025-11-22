from sqlalchemy.exc import SQLAlchemyError
from src.core.stage.model import Stage, StatusStage, CoverageRequest
from src.core import stage as stage_functions
from src.core.database import db

def get_available_stages(project_id: int):
    """
    funcion para obtener las etapas disponibles de un proyecto.
    """
    stages_list = stage_functions.get_available_stages(project_id)
    
    # Convertir los objetos Stage a diccionarios.
    stages_dict = [stage.to_dict() for stage in stages_list]

    # Retornar la lista de etapas como JSON.
    return stages_dict
    
    

def cover_stage(user_id: int, stage_id: int):
    """
    Cubre una etapa específica según su ID.
    """
    try:
        stage = Stage.query.filter_by(id=stage_id, status=StatusStage.PENDING).first()
        if not stage:
            return None
        
        stage.user_id = user_id
        stage.status = StatusStage.IN_PROGRESS
        db.session.commit()
        return stage
    except SQLAlchemyError as error:
        db.session.rollback()
        raise Exception(f"Error al registrar el stage.")


def finish_stage(stage_id: int):
    """
    funcion para finalizar una etapa específica según su ID.
    """
    stage = stage_functions.cover_stage(stage_id)

    # Lógica para indicar que la etapa ya está cubierta.
    if stage:
        if stage.status == StatusStage.IN_PROGRESS:
            stage_functions.set_stage_as_finished(stage_id)
            return True
    return False


def create_stage(data: dict):
    """
    funcion para crear una nueva etapa.
    """
    #DTO_tomodel, se llama a esa función y ella se encarga de formatear los datos
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


def get_all_stages_pending():
    """
    funcion para obtener todas las etapas pendientes de todos los proyectos.
    """
    stages_list = stage_functions.get_all_stages_pending()
    
    # Convertir los objetos Stage a diccionarios.
    stages_dict = [stage.to_dict() for stage in stages_list]

    # Retornar la lista de etapas como JSON.
    return stages_dict


def get_in_progress_stages_for_user(user_id: int):
    """
    Obtiene las etapas en progreso del usuario actual.
    """
    stages = stage_functions.get_in_progress_stages_by_user(user_id)
    return [stage.to_dict() for stage in stages]
