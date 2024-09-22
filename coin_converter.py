from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Dicionário para mapear os nomes completos para abreviações apenas para `to_currency`
crypto_map = {
    'bitcoin': 'btc',
    'ethereum': 'eth',
    'litecoin': 'ltc',
    'ripple': 'xrp',
    # Adicione mais mapeamentos conforme necessário
}

# Função para obter a abreviação da moeda de destino
def get_currency_abbreviation(currency_name):
    return crypto_map.get(currency_name.lower(), currency_name.lower())

# Rota do microserviço para conversão de criptomoedas
@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    amount = float(data.get('amount'))
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')

    # Somente o `to_currency` precisa da abreviação
    to_currency_abbr = get_currency_abbreviation(to_currency)

    # URL da CoinGecko para obter a taxa de conversão
    coingecko_url = f"https://api.coingecko.com/api/v3/simple/price?ids={from_currency}&vs_currencies={to_currency_abbr}"
    response = requests.get(coingecko_url)

    # Verificar se a resposta da API é válida
    if response.status_code != 200:
        return jsonify({'error': 'Erro ao obter taxa de conversão da API CoinGecko.'}), 500

    # Obter a taxa de conversão
    conversion_data = response.json()

    if from_currency not in conversion_data or to_currency_abbr not in conversion_data[from_currency]:
        return jsonify({'error': f'Conversão não encontrada para {from_currency} -> {to_currency}'}), 400

    conversion_rate = conversion_data[from_currency][to_currency_abbr]

    # Calcula o valor convertido
    converted_amount = amount * conversion_rate

    return jsonify({'converted_amount': converted_amount})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
