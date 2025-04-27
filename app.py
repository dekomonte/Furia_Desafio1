from flask import Flask, request, jsonify, send_from_directory
import mysql.connector
import os

app = Flask(__name__, static_folder='public')

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',      # <-- Alterar aqui
    'password': 'Flamengo_2019$@',     # <-- Alterar aqui
    'database': 'furia_chat'     # <-- Nome do Banco de dados
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# Rota para servir o index.html
@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path), 'index.html')

# Rota para servir a imagem da logo (dentro da pasta public)
@app.route('/public/logo.png')
def serve_logo():
    return send_from_directory(os.path.join(app.root_path, 'public'), 'logo.png')

# Rota para servir o arquivo de CSS (dentro da pasta public)
@app.route('/public/style.css')
def serve_css():
    return send_from_directory(os.path.join(app.root_path, 'public'), 'style.css')

# Rota para servir o arquivo de JavaScript (dentro da pasta public)
@app.route('/public/script.js')
def serve_js():
    return send_from_directory(os.path.join(app.root_path, 'public'), 'script.js')

# Endpoint de chat
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    resposta = buscar_resposta(user_message)
    return jsonify({"response": resposta})

def buscar_resposta(mensagem):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT bot_response FROM messages WHERE user_input = %s"
    cursor.execute(query, (mensagem,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result["bot_response"]
    else:
        return "Desculpe, não entendi. Pode reformular?"

# Endpoint para obter todas as perguntas disponíveis
@app.route('/perguntas', methods=['GET'])
def perguntas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT DISTINCT user_input FROM messages"
    cursor.execute(query)
    perguntas_result = cursor.fetchall()

    cursor.close()
    conn.close()

    perguntas_lista = [pergunta["user_input"] for pergunta in perguntas_result]
    return jsonify({"perguntas": perguntas_lista})

if __name__ == "__main__":
    app.run(debug=True)
