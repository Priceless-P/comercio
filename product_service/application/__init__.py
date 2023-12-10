import os
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ['ENVIRONMENT_CONFIGURATION']
    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        from application.product_api import product_api_blueprint
        app.register_blueprint(product_api_blueprint)

        return app
