import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(env_path):
    load_dotenv(env_path)

class Config():
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATION = False

class DevelopmentConfig(Config):
    ENV = 'Development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')

class ProductionConfig(Config):
    ENV = 'Production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')
