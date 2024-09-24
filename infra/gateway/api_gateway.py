from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Função para tentar a rota primária e, se indisponível, tenta a secundária
def try_request(urls, json_data):
    try:
        # Tenta a primeira URL (primária)
        primary_response = requests.post(urls[0], json=json_data)
        if primary_response.status_code == 503:
            raise requests.exceptions.RequestException("Serviço indisponível")
        return primary_response.json(), primary_response.status_code
    except requests.exceptions.RequestException:
        # Se o serviço primário estiver indisponível, tenta a URL secundária
        try:
            secondary_response = requests.post(urls[1], json=json_data)
            return secondary_response.json(), secondary_response.status_code
        except requests.exceptions.RequestException:
            return {"error": "Both primary and secondary services are unavailable"}, 503

# Rota do API Gateway para conversão de Criptos
@app.route('/convert-crypto', methods=['POST'])
def convert_crypto():
    data = request.json
    amount = data.get('amount')
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')

    # URLs primária e secundária para criptos
    urls = [
        "http://localhost:5001/convert-crypto-currency",  # Rota primária
        "http://localhost:5009/convert-crypto-currency"   # Rota secundária
    ]

    response, status_code = try_request(urls, {
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency
    })

    return jsonify(response), status_code

# Rota do API Gateway para conversão de Moedas Reais
@app.route('/convert-real', methods=['POST'])
def convert_real_currency():
    data = request.json
    amount = data.get('amount')
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')

    # URLs primária e secundária para moedas reais
    urls = [
        "http://localhost:5002/convert-real-currency",  # Rota primária
        "http://localhost:5007/convert-real-currency"   # Rota secundária
    ]

    response, status_code = try_request(urls, {
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency
    })

    return jsonify(response), status_code

# Rota do API Gateway para login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # URLs primária e secundária para login
    urls = [
        "http://localhost:5003/login",  # Rota primária
        "http://localhost:5008/login"   # Rota secundária
    ]

    response, status_code = try_request(urls, {
        'email': email,
        'password': password
    })

    return jsonify(response), status_code

# Rota do API Gateway para registro de usuários
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # URLs primária e secundária para registro
    urls = [
        "http://localhost:5004/register-signup",  # Rota primária
        "http://localhost:5006/register-signup"   # Rota secundária
    ]

    response, status_code = try_request(urls, {
        'name': name,
        'email': email,
        'password': password
    })

    return jsonify(response), status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
