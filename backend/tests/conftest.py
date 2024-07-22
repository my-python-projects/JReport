import sys
import os
import pytest

# Adiciona o diretório 'backend' ao caminho de importação do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from log_config import setup_test_logging
from app import create_app

@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "MONGO_URI": os.getenv('MONGO_URI', "mongodb://localhost:27017/jreport")
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def log_tests(request):
    # Configuração do logger
    logger = setup_test_logging()

    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Finished test: {request.node.name}")
