"""Defines User api blueprint"""

from flask import Blueprint

user_api_blueprint = Blueprint('user_api', __name__,)

from application.user_api import routes
