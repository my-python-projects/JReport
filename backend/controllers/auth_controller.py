from flask import request, jsonify
from services.auth_service import register_user, authenticate_user

def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = register_user(db, email, password)
    if user:
        return jsonify({'message': 'User registered successfully!'}), 201
    return jsonify({'error': 'User already exists!'}), 400

def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = authenticate_user(db, email, password)
    if user:
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'error': 'Invalid email or password!'}), 401
