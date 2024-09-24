import json
import bcrypt
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Caminho para o arquivo de banco de dados
database_path = 'dataBase/clients.json'

# Função para carregar o banco de dados (arquivo JSON)
def load_database():
    if os.path.exists(database_path):
        with open(database_path, 'r') as file:
            return json.load(file)
    return []

# Função para salvar no banco de dados (arquivo JSON)
def save_database(users_db):
    with open(database_path, 'w') as file:
        json.dump(users_db, file, indent=4)

@app.route('/register-signup', methods=['POST'])
def register():
    data = request.get_json()

    # Carregar o banco de dados
    users_db = load_database()

    # Verificar se o e-mail já está registrado
    if any(user['email'] == data['email'] for user in users_db):
        return jsonify({'message': 'E-mail já registrado!'}), 400

    # Hash da senha
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    # Armazenar o novo usuário no "banco de dados"
    users_db.append({
        'name': data['name'],
        'email': data['email'],
        'password': hashed_password.decode('utf-8')  # Armazenando a senha hashada como string
    })

    # Salvar o banco de dados atualizado
    save_database(users_db)

    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

if __name__ == '__main__':
    # Cria o diretório se não existir
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
    
    app.run(host='0.0.0.0', port=5006)
