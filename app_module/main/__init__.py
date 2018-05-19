from flask import Blueprint

bp = Blueprint('main', __name__)

from app_module.main import routes