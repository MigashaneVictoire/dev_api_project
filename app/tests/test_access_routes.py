import os,sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from routes.access_routes import app, users

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    users.clear()  # reset users between tests


def test_register_and_login(client):
    # Register
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['success'] is True

    # Login
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True


def test_logout(client):
    # Register and login
    client.post('/register', json={'username': 'testuser', 'password': 'password123'})
    client.post('/login', json={'username': 'testuser', 'password': 'password123'})

    # Logout
    response = client.post('/logout')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
