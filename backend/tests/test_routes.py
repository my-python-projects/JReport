import pytest
import logging
from app import create_app

# Usar o logger de teste configurado
logger = logging.getLogger('test')

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_register_route(client):
    logger.info("Testing register route")
    
    response = client.post('/api/register', json={
        'username': 'newuser',
        'password': 'Newpassword33@',
        'email': 'newuser@example.com'
    })
    
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    logger.info("Register route test passed")


def test_login_route(client):
    logger.info("Testing login route")
    
    response = client.post('/api/login', json={
        'email': 'newuser@example.com',
        'password': 'Newpassword33@'
    })
    
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    logger.info("Login route test passed")


def test_error_login_route(client):
    logger.info("Testing error in login route")
    
    response = client.post('/api/login', json={
        'email': 'newuser1@example.com',
        'password': 'newpassword33@'
    })
    
    assert response.status_code == 401, f"Expected status code 401 but got {response.status_code}"
    logger.info("Erro in Login route test passed")
