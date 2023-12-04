# test/test_post_endpoints.py
import pytest
import sys
sys.path.append("/mnt/c/Users/rsrin/my_flask_project/")  # Add the path to your project directory

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_create_tweet_success(client):
    response = client.post('/tweets', json={'text': 'Test tweet'})
    assert response.status_code == 201
    assert 'id' in response.json  # Check if the response contains the 'id' field
    assert 'text' in response.json  # Check if the response contains the 'text' field
