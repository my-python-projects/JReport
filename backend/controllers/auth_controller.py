from flask import jsonify, request, current_app
from services.auth_service import create_user, authenticate_user
from utils.mongo import mongo

def register_user(request):
    try:
        db = mongo.db
        email = request.json.get('email')
        password = request.json.get('password')
        
        print(f"Registering user with email: {email}")
        
        result = create_user(db, email, password)
        if result:
            return jsonify({'success': True, 'message': 'User registered successfully'}), 200
        else:
            return jsonify({'success': False, 'message': 'Registration failed'}), 400
    except Exception as e:
        print(f"Error in register_user: {e}")
        return jsonify({'success': False, 'message': 'Internal server error'}), 500

def login_user(request):
    try:
        db = mongo.db
        email = request.json.get('email')
        password = request.json.get('password')
        
        print(f"Logging in user with email: {email}")
        
        result = authenticate_user(db, email, password)
        if result:
            return jsonify({'success': True, 'message': 'Login successful'}), 200
        else:
            return jsonify({'success': False,'message': 'Invalid credentials'}), 401
    except Exception as e:
        print(f"Error in login_user: {e}")
        return jsonify({'success': False, 'message': 'Internal server error'}), 500
