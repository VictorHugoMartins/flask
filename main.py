from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

exclusive_airbnb_columns = ['host_id', 'name', 'minstay', 'bathroom', 'avg_rating', 'extra_host_languages', 'is_superhost', 'room_type']
exclusive_booking_columns = ['start_date', 'finish_date']

app = Flask(__name__) # Dados de usuário armazenados em um dicionário
CORS(app)

@app.route('/')
def h(): # Recebe o username e password do request em formato json
	return jsonify({"message": "Erro ao retornar colunas para seleção de dados para coleta!", "success": False}), 500 # Inicia a aplicação

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)
