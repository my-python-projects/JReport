from flask import Flask

# Inicialização do aplicativo Flask
app = Flask(__name__)

# Configuração básica do logger
import logging
import os

LOG_DIR        = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs')
LOG_FILE       = os.path.join(LOG_DIR, 'app.log')
#LOG_FILE_DEBUG = os.path.join(LOG_DIR, 'debug.log')


if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
#logging.basicConfig(filename=LOG_FILE_DEBUG, level=logging.DEBUG)

# Importação de rotas para registrar rotas
from app import routes
