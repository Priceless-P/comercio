from flask import Blueprint

product_api_blueprint = Blueprint('product_api', __name__)

from application.product_api import routes
