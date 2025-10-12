from dotenv import load_dotenv
from datetime import timedelta
import os
load_dotenv()

class Config(object):
    """
    Configuración base.
    """
    
    SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProductionConfig(Config):
    """
    Configuración de producción.
    """
    SQLALCHEMY_DATABASE_URI = "postgresql://user_marcos:SOwifBUGthtEy3SjK94CvOiF4imhVcnD@dpg-d3lpnnmmcj7s73a4rtpg-a/db_cloud_h6f4"


class DevelopmentConfig(Config):
    """
    Configuración de desarrollo.
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DB_URL",
        "postgresql://postgres:postgres@localhost:5432/db_nube"
    )


class TestingConfig(Config):
    """Configuración de testing."""
    
    TESTING = True
    
    
config  = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestingConfig,
}