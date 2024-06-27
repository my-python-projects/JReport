from flask import Flask
from flask_cors import CORS
from config import Config
from utils.mongo import mongo, init_mongo

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o MongoDB
    init_mongo(app)

    # Configura o CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from routes.auth_routes import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
