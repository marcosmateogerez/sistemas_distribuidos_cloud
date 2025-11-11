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
    SQLALCHEMY_DATABASE_URI = "postgresql://db_cloud_2z6z_user:rmWcKfQWz80pYxFYD2rB7aihW2yFaZWA@dpg-d49sed75r7bs73e2fq80-a/db_cloud_2z6z"


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