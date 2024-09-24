from flask import Flask, request, jsonify
import json
import os
import bcrypt

app = Flask(__name__)

# Caminho para o arquivo de banco de dados
database_path = 'dataBase/clients.json'

# Função para carregar o banco de dados (arquivo JSON)
def load_database():
    if os.path.exists(database_path):
        with open(database_path, 'r') as file:
            return json.load(file)
    return []

@app.route('/login', methods=['POST'])
def login():
    # Captura o corpo da requisição como JSON
    data = request.get_json()

    # Obtém o email e senha enviados
    email = data.get('email')
    password = data.get('password')

    # Carrega o banco de dados de usuários do arquivo JSON
    users_db = load_database()

    # Verifica se o email existe no banco de dados
    user = next((user for user in users_db if user['email'] == email), None)

    if user:
        # Hash armazenado no arquivo JSON
        stored_hash = user['password'].encode('utf-8')
        print(password.encode('utf-8'))
        print(stored_hash)

        # Compara o hash da senha fornecida pelo usuário com o hash armazenado
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            return jsonify({"message": "Login realizado com sucesso!", "status": "success"}), 200
        else:
            return jsonify({"message": "Credenciais inválidas!", "status": "error"}), 401
    else:
        return jsonify({"message": "Credenciais inválidas!", "status": "error"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
