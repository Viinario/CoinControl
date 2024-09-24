from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Definindo taxas de câmbio fixas (valores atuais)
conversion_rates = {
    'usd_to_eur': 0.85,   # Dólar Americano para Euro
    'usd_to_brl': 5.30,   # Dólar Americano para Real Brasileiro
    'eur_to_usd': 1.18,   # Euro para Dólar Americano
    'eur_to_brl': 6.20,   # Euro para Real Brasileiro
    'brl_to_usd': 0.19,   # Real Brasileiro para Dólar Americano
    'brl_to_eur': 0.16,   # Real Brasileiro para Euro
    'brl_to_brl':  1,     # Real Brasileiro para Real Brasileiro
    'eur_to_eur':  1,    # Euro para Euro
    'usd_to_usd':  1     # Dólar Americano para Dólar Americano
}

# Função para converter o valor baseado nas taxas definidas
def convert_real_currency(amount, from_currency, to_currency):
    key = f'{from_currency.lower()}_to_{to_currency.lower()}'
    conversion_rate = conversion_rates.get(key)

    if conversion_rate is None:
        return None

    return amount * conversion_rate

# Rota para o microserviço de conversão de moedas reais (nova rota)
@app.route('/convert-real-currency', methods=['POST'])
def convert():
    data = request.json
    try:
        amount = float(data.get('amount'))  # Converte o valor para float
    except (ValueError, TypeError):
        return jsonify({'error': 'O valor fornecido para conversão é inválido'}), 400

    from_currency = data.get('from_currency').upper()  # Certifica-se de que está em maiúsculas
    to_currency = data.get('to_currency').upper()

    # Validação básica dos parâmetros
    if not all([amount, from_currency, to_currency]):
        return jsonify({'error': 'Parâmetros inválidos'}), 400

    # Realiza a conversão
    result = convert_real_currency(amount, from_currency, to_currency)

    if result is None:
        return jsonify({'error': 'Conversão não suportada'}), 400

    # Formatando o valor convertido com duas casas decimais
    converted_amount = f"{result:.2f}"
    exchange_rate = f"{conversion_rates[f'{from_currency.lower()}_to_{to_currency.lower()}']:.2f}"

    return jsonify({
        'from_currency': from_currency,
        'to_currency': to_currency,
        'original_amount': f"{amount:.2f}",
        'converted_amount': converted_amount,
        'exchange_rate': exchange_rate
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
