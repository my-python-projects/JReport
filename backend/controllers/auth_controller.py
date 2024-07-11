from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import create_user, authenticate_user, generate_qr_code, enable_2fa, is_2fa_enabled
from utils.mongo import mongo

def register_user():
    try:
        db          = mongo.db
        username    = request.json.get('username')
        email       = request.json.get('email')
        password    = request.json.get('password')

        print(f"Registering user {username} with email: {email}")

        sucess, secret = create_user(db, username, email, password)

        if sucess:
            qr_code    = generate_qr_code(secret, email)
            return jsonify({ 
                'success': True, 
                'message': 'User registered successfully', 
                'qr_code': f'data:image/png;base64,{qr_code}',
                'email'  : email  # Retorna o email para a verificação do 2FA
            }), 200
        else:
            return jsonify({ 'success': False, 'message': 'Registration failed'}), 400
        
    except Exception as e:
        print(f"Error in register_user: {e}")
        return jsonify({ 'success': False, 'message': 'Internal server error' }), 500

def login_user():
    try:
        db          = mongo.db
        email       = request.json.get('email')
        password    = request.json.get('password')
        token_2fa   = request.json.get('token_2fa')

        print(f"Logging in user with email: {email}")

        response, error = authenticate_user(db, email, password, token_2fa)

        if error:
            if error == '2FA required':
                return jsonify({ 'success': False, 'message': '2FA required', 'require_2fa': True }), 401
            else:
                return jsonify({ 'success': False, 'message': error }), 401
        else:
            return jsonify(response), 200
        
    except Exception as e:
        print(f"Error in login_user: {e}")
        return jsonify({ 'success': False, 'message': 'Internal server error' }), 500

def verify_2fa():
    try:
        db          = mongo.db
        email       = request.json.get('email')
        token_2fa   = request.json.get('token_2fa')

        print(f"Verifying 2FA for user with email: {email}")

        success, error = enable_2fa(db, email, token_2fa)

        if success:
            return jsonify({ 'success': True, 'message': '2FA enabled successfully' }), 200
        else:
            return jsonify({ 'success': False, 'message': error }), 400

    except Exception as e:
        print(f"Error in verify_2fa: {e}")
        return jsonify({ 'success': False, 'message': 'Internal server error' }), 500

from services.auth_service import is_2fa_enabled


def check_2fa():
    try:
        db          = mongo.db
        email       = request.json.get('email')

        print(f"Checking 2FA for user with email: {email}")

        is_enabled, error = is_2fa_enabled(db, email)

        if error:
            return jsonify({ 'success': False, 'message': error }), 400
        else:
            return jsonify({ 'success': True, 'enabled_2fa': is_enabled }), 200

    except Exception as e:
        print(f"Error in check_2fa: {e}")
        return jsonify({ 'success': False, 'message': 'Internal server error' }), 500


@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200