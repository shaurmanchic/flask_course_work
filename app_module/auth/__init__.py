from flask import Blueprint

bp = Blueprint('auth', __name__)

from app_module.auth import routes