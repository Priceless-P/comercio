import os
import config
from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from monitoring.metrics import metrics_blueprint
from monitoring.health import health_blueprint
from flask_swagger_ui import get_swaggerui_blueprint


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ['ENVIRONMENT_CONFIGURATION']
    app.config.from_object(environment_configuration)

    db.init_app(app)
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.yml'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Product Service",
            'title': 'Product API Documentation',
            'uiversion': 3,
        '   openapi': '3.0.2'
        }
    )
    Swagger(app)
    with app.app_context():
        from application.product_api import product_api_blueprint
        app.register_blueprint(product_api_blueprint)
        app.register_blueprint(metrics_blueprint)
        app.register_blueprint(health_blueprint)
        app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

        return app
