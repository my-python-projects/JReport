from flask import Flask

# Inicialização do aplicativo Flask
app = Flask(__name__)

# Importação de rotas para registrar rotas
from app import routes
