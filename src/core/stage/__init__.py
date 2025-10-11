from src.core.stage.model import Stage
from src.core.database import db
from src.core.stage.model import status as status_stage
from flask import jsonify




def get_available_stages(project_id: int):
    """
    funcion para obtener las etapas disponibles de un proyecto.
    """
    stages_list = Stage.query.filter_by(id_project=project_id, status=status_stage.PENDING).all()
    return stages_list
   
   
   
def cover_stage(stage_id: int):
    """
    funcion para cubrir una etapa específica según su ID.
    """
    stage = Stage.query.get(stage_id)

    # Lógica para indicar que la etapa ya está cubierta
    return stage
    
    

def set_stage_in_progress(stage_id: int):
    """
    funcion para cambiar el estado de una etapa a "IN_PROGRESS".
    """
    stage = Stage.query.get(stage_id)
    if stage:
        stage.status = status_stage.IN_PROGRESS
        db.session.commit()
        return stage
    return None


def set_stage_as_finished(stage_id: int):
    """
    funcion para cambiar el estado de una etapa a "FINISHED".
    """
    stage = Stage.query.get(stage_id)
    if stage:
        stage.status = status_stage.FINISHED
        db.session.commit()
        return stage
    return None