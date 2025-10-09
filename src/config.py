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
    pass


class DevelopmentConfig(Config):
    """
    Configuración de desarrollo.
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DB_URL",
        "postgresql://postgres:postgres@localhost:5432/db_nube"
    )


class TestingConfig(Config):
    """Production configuration."""
    
    TESTING = True
    
    
config  = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestingConfig,
}