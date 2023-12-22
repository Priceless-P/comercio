from flask import Blueprint


metrics_blueprint = Blueprint('metrics', __name__)
health_blueprint = Blueprint('health', __name__)
