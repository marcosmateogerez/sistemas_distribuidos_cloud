from werkzeug.exceptions import BadRequest

def validate_observation_data(data):
    """
    Valida si se recibieron los datos "name" y "description".
    """
    if not data:
        raise BadRequest("No se enviaron datos")
    if "name" not in data or "description" not in data:
        raise BadRequest("Faltan campos obligatorios")
    return data["name"], data["description"]