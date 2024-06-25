from flask import Blueprint
from controllers.auth_controller import register, login

auth_blueprint = Blueprint('auth', __name__)

auth_blueprint.route('/api/register', methods=['POST'])(register)
auth_blueprint.route('/api/login', methods=['POST'])(login)

