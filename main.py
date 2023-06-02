from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from general_config import ABConfig
import search
from file_manager import export_datatable
from general_dict import columnDict, get_airbnb_rooms_by_ss_id, get_booking_rooms_by_ss_id, get_all_rooms_by_ss_id
from utils import select_command, insert_command, update_command
from utils import buildChartObjectFromValueCounts, send_nullable_value
from utils import removeLastWordOfString, buildFilterQuery, asSelectObject, build_options
from thread import Th

ab_config = ABConfig()

exclusive_airbnb_columns = ['host_id', 'name', 'minstay', 'bathroom', 'avg_rating', 'extra_host_languages', 'is_superhost', 'room_type']
exclusive_booking_columns = ['start_date', 'finish_date']

app = Flask(__name__) # Dados de usuário armazenados em um dicionário
CORS(app)

@app.route('/')
def h(): # Recebe o username e password do request em formato json
	return jsonify({"message": "Erro ao retornar colunas para seleção de dados para coleta!", "success": False}), 500 # Inicia a aplicação

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)
