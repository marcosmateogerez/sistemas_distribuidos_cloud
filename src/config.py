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

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_URL = os.getenv("DB_URL")


class TestingConfig(Config):
    """Production configuration."""
    
    TESTING = True
    
    
config  = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestingConfig,
}