from flask import Blueprint

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
def index():
    return "Welcome to the Store API!"