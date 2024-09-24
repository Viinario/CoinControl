from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Importa a biblioteca CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Rota do API Gateway para conversão de Criptos
@app.route('/convert-crypto', methods=['POST'])
def convert_crypto():
    data = request.json
    amount = data.get('amount')
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')

    # Chama o microserviço de conversão de criptomoedas
    conversion_service_url = "http://localhost:5001/convert-crypto-currency"  # Rota para criptos
    response = requests.post(conversion_service_url, json={
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency
    })
    
    return jsonify(response.json()), response.status_code

# Rota do API Gateway para conversão de Moedas Reais
@app.route('/convert-real', methods=['POST'])
def convert_real_currency():
    data = request.json
    amount = data.get('amount')
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')

    # Chama o microserviço de conversão de moedas reais
    conversion_service_url = "http://localhost:5002/convert-real-currency"  # Nova rota para moedas reais
    response = requests.post(conversion_service_url, json={
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency
    })
    return jsonify(response.json()), response.status_code

# Rota do API Gateway para login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Chama o microserviço de login
    login_service_url = "http://localhost:5003/login"  # Rota para o microserviço de login
    response = requests.post(login_service_url, json={
        'email': email,
        'password': password
    })

    return jsonify(response.json()), response.status_code

# Rota do API Gateway para registro de usuários
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Chama o microserviço de registro
    register_service_url = "http://localhost:5004/register-signup"  # URL do microserviço de registro
    response = requests.post(register_service_url, json={
        'name': name,
        'email': email,
        'password': password
    })

    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

