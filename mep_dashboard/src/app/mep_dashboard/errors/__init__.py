from flask import Blueprint

errors = Blueprint('errors', __name__)

from app.mep_dashboard.errors import handlers
