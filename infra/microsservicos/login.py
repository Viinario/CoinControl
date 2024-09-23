from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um "banco de dados" de usuários com e-mails e senhas
users_db = {
    "vinicius@ufrpe.com": "1234567",
}

@app.route('/login', methods=['POST'])
def login():
    # Captura o corpo da requisição como JSON
    data = request.get_json()

    # Obtém o email e senha enviados
    email = data.get('email')
    password = data.get('password')

    # Verifica se o usuário existe no "banco de dados"
    if email in users_db and users_db[email] == password:
        return jsonify({"message": "Login realizado com sucesso!", "status": "success"}), 200
    else:
        return jsonify({"message": "Credenciais inválidas!", "status": "error"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
