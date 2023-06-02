from flask import Flask, request, jsonify

app = Flask(__name__) # Dados de usuário armazenados em um dicionário

@app.route('/')
def index():
	response = jsonify({"message": "Erro ao retornar colunas para seleção de dados para coleta!", "success": False}), 500 # Inicia a aplicação
	response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/a')
def h(): # Recebe o username e password do request em formato json
	return "hello"

if __name__ == '__main__':
  app.run(port=5000)
