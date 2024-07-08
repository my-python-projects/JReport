from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import create_user, authenticate_user, generate_tokens, verify_2fa_token
from utils.mongo import mongo

def register_user():
    try:
        db          = mongo.db
        username    = request.json.get('username')
        email       = request.json.get('email')
        password    = request.json.get('password')

        print(f"Registering user {username} with email: {email}")

        result = create_user(db, username, email, password)

        if result:
            return jsonify({'success': True, 'message': 'User registered successfully'}), 200
        else:
            return jsonify({'success': False, 'message': 'Registration failed'}), 400
        
    except Exception as e:
        print(f"Error in register_user: {e}")
        return jsonify({'success': False, 'message': 'Internal server error'}), 500

def login_user():
    try:
        db          = mongo.db
        email       = request.json.get('email')
        password    = request.json.get('password')
        token_2fa   = request.json.get('token_2fa')

        print(f"Logging in user with email: {email}")

        user = authenticate_user(db, email, password)

        if user and verify_2fa_token(user['2fa_secret'], token_2fa):
            access_token, refresh_token = generate_tokens(user)
            return jsonify({'success': True, 
                            'access_token': access_token, 
                            'refresh_token': refresh_token, 
                            'message': 'Login successful'}), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials or 2FA token'}), 401
        
    except Exception as e:
        print(f"Error in login_user: {e}")
        return jsonify({'success': False, 'message': 'Internal server error'}), 500

@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
