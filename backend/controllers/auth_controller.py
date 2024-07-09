from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import create_user, authenticate_user, generate_tokens, verify_2fa_token, generate_qr_code
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
            # Gerar o QR Code
            qr_code         = generate_qr_code(secret, email)
            return jsonify({ 
                'success': True, 
                'message': 'User registered successfully', 
                'qr_code': f'data:image/png;base64,{qr_code}'}), 200
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
                return jsonify({ 'success': False, 'message': '2FA required' }), 401
            else:
                return jsonify({ 'success': False, 'message': error }), 401
        else:
            return jsonify(response), 200
        
    except Exception as e:
        print(f"Error in login_user: {e}")
        return jsonify({ 'success': False, 'message': 'Internal server error' }), 500

@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
