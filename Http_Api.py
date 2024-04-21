# app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_gists():
    username = 'octocat'
    url = f'https://api.github.com/users/{username}/gists'
    response = requests.get(url)
    
    if response.status_code == 200:
        gists = response.json()
        return jsonify(gists)
    else:
        return jsonify({'error': 'Failed to fetch gists'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
