from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Importa a biblioteca CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Rota do API Gateway para conversão de Criptos
@app.route('/convert-currency', methods=['POST'])
def convert_bitcoin_ethereum():
    data = request.json
    amount = data.get('amount')
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')

    # Chama o microserviço de conversão
    conversion_service_url = "http://localhost:5001/convert"
    response = requests.post(conversion_service_url, json={
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency
    })
    
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
