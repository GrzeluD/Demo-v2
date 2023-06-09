from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/endpoint', methods=['POST'])
def handle_request():
    data = request.get_json()
    response = requests.post('https://example.com/api', json=data)
    result = response.json()
    return jsonify(result)

if __name__ == '__main__':
    app.run()