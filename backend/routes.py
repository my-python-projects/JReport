from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend/public')
CORS(app)

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validação simples da senha (mínimo 6 caracteres, pelo menos uma maiúscula e um caracter especial)
    if len(password) < 6 or not any(char.isupper() for char in password) or not any(char in '!@#$%^&*()-_=+[{]};:\'",<.>/?' for char in password):
        return jsonify({'error': 'A senha deve ter no mínimo 6 caracteres, pelo menos uma letra maiúscula e um caracter especial'}), 400

    # Aqui você pode implementar a lógica para salvar o usuário no banco de dados, por exemplo

    # Simulação de resposta de sucesso
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 200


@app.route('/api/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Simulação de verificação de login (aqui você deve verificar no banco de dados)
    if email == "user@example.com" and password == "Password@123":
        return jsonify({'message': 'Login realizado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Credenciais inválidas'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
