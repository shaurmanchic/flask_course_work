from flask import Blueprint

bp = Blueprint('errors', __name__)

from app_module.errors import handlers