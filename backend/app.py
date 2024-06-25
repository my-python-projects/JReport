from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Conexão com o MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client.get_database()

# Importando e registrando as rotas
from routes import auth_blueprint
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=True)


# Configura o caminho para os templates
#template_path       = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'templates')
#app.template_folder = template_path