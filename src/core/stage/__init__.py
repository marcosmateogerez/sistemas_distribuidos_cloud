from src.core.stage.model import Stage, StatusStage
from src.core.database import db

def get_available_stages(project_id: int):
    """
    funcion para obtener las etapas disponibles de un proyecto.
    """
    stages_list = Stage.query.filter_by(id_project=project_id, status=StatusStage.PENDING).all()
    return stages_list

   
def cover_stage(stage_id: int):
    """
    funcion para cubrir una etapa específica según su ID.
    """
    stage = Stage.query.get(stage_id)

    # Lógica para indicar que la etapa ya está cubierta.
    return stage


def set_stage_in_progress(stage_id: int):
    """
    funcion para cambiar el estado de una etapa a "IN_PROGRESS".
    """
    stage = Stage.query.get(stage_id)
    if stage:
        stage.status = StatusStage.IN_PROGRESS
        db.session.commit()
        return stage
    return None


def set_stage_as_finished(stage_id: int):
    """
    funcion para cambiar el estado de una etapa a "FINISHED".
    """
    stage = Stage.query.get(stage_id)
    if stage:
        stage.status = StatusStage.FINISHED
        db.session.commit()
        return stage
    return None


def create_stage(new_stage: Stage):
    """
    funcion para crear una nueva etapa.
    """
    new_stage.status = StatusStage.PENDING
    db.session.add(new_stage)
    db.session.commit()
    return new_stage or None

def get_all_stages_pending():
    """
    funcion para obtener todas las etapas pendientes.
    """
    stages_list = Stage.query.filter_by(status=StatusStage.PENDING).all()
    return stages_list


def get_in_progress_stages_by_user(user_id: int):
    """
    Retorna todas las etapas que están en progreso (IN_PROGRESS)
    asignadas a un usuario específico.
    """
    stages = Stage.query.filter_by(user_id=user_id, status=StatusStage.IN_PROGRESS).all()
    return stages
