from flask import Flask, request, jsonify
import json
import os
import bcrypt

app = Flask(__name__)

# Função para carregar o banco de dados de clientes a partir de um arquivo JSON
def load_users_db():
    # Define o caminho completo para o arquivo clients.json
    file_path = os.path.join(os.path.dirname(__file__), 'dataBase/clients.json')

    # Abre o arquivo e carrega os dados
    with open(file_path, 'r') as f:
        users_db = json.load(f)

    return users_db

@app.route('/login', methods=['POST'])
def login():
    # Captura o corpo da requisição como JSON
    data = request.get_json()

    # Obtém o email e senha enviados
    email = data.get('email')
    password = data.get('password')

    # Carrega o banco de dados de usuários do arquivo JSON
    users_db = load_users_db()

    # Verifica se o email existe no banco de dados
    if email in users_db:
        # Hash armazenado no arquivo JSON
        stored_hash = users_db[email].encode('utf-8')
        print(bcrypt.checkpw(password.encode('utf-8'), stored_hash))

        # Gera o hash da senha fornecida pelo usuário e compara com o hash armazenado
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            return jsonify({"message": "Login realizado com sucesso!", "status": "success"}), 200
        else:
            return jsonify({"message": "Credenciais inválidas!", "status": "error"}), 401
    else:
        return jsonify({"message": "Credenciais inválidas!", "status": "error"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
