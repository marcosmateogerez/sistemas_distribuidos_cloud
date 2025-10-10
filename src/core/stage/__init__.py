from src.core.stage.model import Stage
from src.core.database import db
from flask import jsonify




def get_available_stages(project_id: int):
    """
    Endpoint para obtener las etapas disponibles de un proyecto.
    """
    stages_list = Stage.query.filter_by(id_project=project_id).all()
    print("STAGES DISPONIBLES" , stages_list)
    if not stages_list:
        return jsonify({"message": "No se encontraron etapas para el proyecto especificado."}), 404

    # Convertir los objetos Stage a diccionarios
    stages_dict = [stage.to_dict() for stage in stages_list]

    # Retornar la lista de etapas como JSON
    return jsonify(stages_dict)
    