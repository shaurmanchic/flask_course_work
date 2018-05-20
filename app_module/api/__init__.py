from flask import Blueprint

bp = Blueprint('api', __name__)

from app_module.api import users, errors, tokens