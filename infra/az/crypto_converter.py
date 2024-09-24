from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Dicionário para mapear os nomes completos para abreviações apenas para `to_currency`
crypto_map = {
    'bitcoin': 'btc',
    'ethereum': 'eth',
    'litecoin': 'ltc',
    'ripple': 'xrp',
    'dolar': 'usd',
    'euro': 'eur',
    'real': 'brl',
}

# Dicionário com as taxas de conversão predefinidas, incluindo de uma moeda para ela mesma (valor = 1)
conversion_rates = {
    'bitcoin': {
        'bitcoin': 1,
        'ethereum': 24.514863,
        'litecoin': 931.782,
        'ripple': 108238,
        'dolar': 30000,          # 1 bitcoin = 30,000 USD
        'euro': 27000,           # 1 bitcoin = 27,000 EUR
        'real': 150000           # 1 bitcoin = 150,000 BRL
    },
    'ethereum': {
        'ethereum': 1,
        'bitcoin': 0.0408049,
        'litecoin': 38.0125,
        'ripple': 4414.87,
        'dolar': 2000,           # 1 ethereum = 2,000 USD
        'euro': 1800,            # 1 ethereum = 1,800 EUR
        'real': 10000            # 1 ethereum = 10,000 BRL
    },
    'litecoin': {
        'litecoin': 1,
        'bitcoin': 0.001073,
        'ethereum': 0.02631,
        'ripple': 116.07,
        'dolar': 100,            # 1 litecoin = 100 USD
        'euro': 90,              # 1 litecoin = 90 EUR
        'real': 500              # 1 litecoin = 500 BRL
    },
    'ripple': {
        'ripple': 1,
        'bitcoin': 0.00000924,
        'ethereum': 0.000226,
        'litecoin': 0.00862,
        'dolar': 0.5,            # 1 ripple = 0.5 USD
        'euro': 0.45,            # 1 ripple = 0.45 EUR
        'real': 2.5              # 1 ripple = 2.5 BRL
    },
    'dolar': {
        'dolar': 1,
        'bitcoin': 0.000033,     # 1 USD = 0.000033 bitcoin
        'ethereum': 0.0005,      # 1 USD = 0.0005 ethereum
        'litecoin': 0.01,        # 1 USD = 0.01 litecoin
        'ripple': 2,             # 1 USD = 2 ripple
        'euro': 0.9,             # 1 USD = 0.9 EUR
        'real': 5                # 1 USD = 5 BRL
    },
    'euro': {
        'euro': 1,
        'bitcoin': 0.000037,     # 1 EUR = 0.000037 bitcoin
        'ethereum': 0.000555,    # 1 EUR = 0.000555 ethereum
        'litecoin': 0.0111,      # 1 EUR = 0.0111 litecoin
        'ripple': 2.22,          # 1 EUR = 2.22 ripple
        'dolar': 1.11,           # 1 EUR = 1.11 USD
        'real': 5.5              # 1 EUR = 5.5 BRL
    },
    'real': {
        'real': 1,
        'bitcoin': 0.0000067,    # 1 BRL = 0.0000067 bitcoin
        'ethereum': 0.0001,      # 1 BRL = 0.0001 ethereum
        'litecoin': 0.002,       # 1 BRL = 0.002 litecoin
        'ripple': 0.4,           # 1 BRL = 0.4 ripple
        'dolar': 0.2,            # 1 BRL = 0.2 USD
        'euro': 0.18             # 1 BRL = 0.18 EUR
    }
}

# Rota do microserviço para conversão de criptomoedas e moedas reais
@app.route('/convert-crypto-currency', methods=['POST'])
def convert():
    data = request.json
    amount = float(data.get('amount'))
    from_currency = data.get('from_currency').lower()
    to_currency = data.get('to_currency').lower()

    # Verifica se as moedas estão no dicionário de conversões
    if from_currency not in conversion_rates or to_currency not in conversion_rates[from_currency]:
        return jsonify({'error': f'Conversão não encontrada para {from_currency} -> {to_currency}'}), 400

    # Obtém a taxa de conversão
    conversion_rate = conversion_rates[from_currency][to_currency]

    # Calcula o valor convertido
    converted_amount = amount * conversion_rate

    return jsonify({'converted_amount': converted_amount})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
