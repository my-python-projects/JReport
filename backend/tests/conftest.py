import sys
import os
import pytest

# Adiciona o diretório 'backend' ao caminho de importação do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from log_config import setup_test_logging

@pytest.fixture(autouse=True)
def log_tests(request):
    # Configuração do logger
    logger = setup_test_logging()

    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Finished test: {request.node.name}")
