from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.auth_controller import register_user, login_user, verify_2fa, check_2fa,protected

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/api/register', methods=['POST'])
def register():
    return register_user()

@auth_blueprint.route('/api/login', methods=['POST'])
def login():
    return login_user()

@auth_blueprint.route('/api/verify-2fa', methods=['POST'])
def verify2fa():
    return verify_2fa()

@auth_blueprint.route('/api/check-2fa', methods=['POST'])
def check_2fa_route():
    return check_2fa()

@auth_blueprint.route('/api/protected', methods=['GET'])
@jwt_required()
def protected_route():
    return protected()
