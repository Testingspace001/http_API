# test_app.py
import requests

def test_get_gists():
    response = requests.get('http://localhost:8080/')
    assert response.status_code == 200
    assert len(response.json()) > 0