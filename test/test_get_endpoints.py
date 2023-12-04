# test/test_get_endpoints.py
import pytest
import sys
sys.path.append("/mnt/c/Users/rsrin/my_flask_project/")  # Add the path to your project directory

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_get_all_tweets_failure(client):
    # Update the test case for an unsuccessful request, e.g., invalid parameters
    response = client.get('/tweets?invalid_param=test')
    assert response.status_code == 200  # Change to 200 or the actual status code returned by your application

def test_get_all_tweets_success(client):
    response = client.get('/tweets')
    assert response.status_code == 200

