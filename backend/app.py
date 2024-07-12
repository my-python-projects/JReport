from flask import Flask
from flask_cors import CORS
from config import Config
from utils.mongo import init_mongo
from flask_jwt_extended import JWTManager
from backend.log_config import setup_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o MongoDB
    init_mongo(app)

    # Inicializa o JWT
    jwt = JWTManager(app)

    # Configura o CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from routes.auth_routes import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

app = create_app()

# Configurar o logging
logger = setup_logging()

if __name__ == '__main__':
    logger.info("Iniciando a aplicação...")
    app.run(debug=True)
