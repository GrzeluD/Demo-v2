from flask import Flask, jsonify, request
from google.cloud import vision
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Wczytaj zmienne środowiskowe z pliku .env
load_dotenv('.env')

# Pobierz klucz uwierzytelniający z zmiennej środowiskowej
vision_api_key = os.environ.get('VISION_API_KEY')

# Inicjalizacja klienta Vision API z uwzględnieniem klucza uwierzytelniającego
credentials = service_account.Credentials.from_service_account_info(vision_api_key)
client = vision.ImageAnnotatorClient(credentials=credentials)
@app.route('/api/endpoint', methods=['POST'])
def handle_request():
    # Odczytaj dane z żądania
    data = request.get_json()

    # Przygotuj dane obrazu do analizy
    image_data = data['imageData']  # Dane obrazu w formacie base64
    image = vision.Image(content=image_data)

    # Wykonaj żądanie do Vision API
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Przygotuj odpowiedź
    result = [label.description for label in labels]

    # Zwróć odpowiedź jako JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run()