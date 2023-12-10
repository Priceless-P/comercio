import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(env_path):
    load_dotenv(env_path)

class Config():
    SQL_TRACK_MODIFICATION = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')
    ENV = 'Development'
    DEBUG = True

class ProductionConfig(Config):
    ENV = 'Production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')