# tests/test_routes.py
from app import app
import json

def test_hello_world():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello World!"

def test_get_all_tweets():
    client = app.test_client()
    response = client.get('/tweets')
    assert response.status_code == 200
    assert response.json is not None

def test_filter_tweets():
    client = app.test_client()
    response = client.get('/tweets/filter?query=Tweet')
    assert response.status_code == 200
    assert response.json is not None

def test_get_tweet_by_id():
    client = app.test_client()
    response = client.get('/tweet/1')
    assert response.status_code == 200
    assert response.json is not None

def test_create_tweet_success():
    client = app.test_client()
    tweet_data = {"text": "New tweet"}
    response = client.post('/tweets', json=tweet_data)
    assert response.status_code == 201
    assert response.json is not None

def test_create_tweet_missing_text():
    client = app.test_client()
    tweet_data = {}  # Missing 'text' field
    response = client.post('/tweets', json=tweet_data)
    assert response.status_code == 400
    assert response.json is not None

def test_create_tweet_bad_request():
    client = app.test_client()
    tweet_data = "Not a dictionary"  # Bad request data
    response = client.post('/tweets', data=tweet_data)
    assert response.status_code == 400
    assert response.json is not None
