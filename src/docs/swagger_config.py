from flasgger import Swagger 
import os
import yaml

def init_swagger(app):
    """
    Inicializa Flasgger leyendo el archivo swagger.yaml completo.
    """
    yaml_path = os.path.join(os.path.dirname(__file__), "swagger.yaml")
    
    with open(yaml_path, "r", encoding="utf-8") as f:
        swagger_template = yaml.safe_load(f)

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    Swagger(app, template=swagger_template, config=swagger_config)