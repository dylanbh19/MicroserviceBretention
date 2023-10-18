# model_api_service.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MODEL_API_ENDPOINT = 'http://model-api-endpoint'

@app.route('/send-to-model', methods=['POST'])
def send_to_model():
    data = request.json
    response = requests.post(MODEL_API_ENDPOINT, json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5001)
