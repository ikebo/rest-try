from flask import Flask, jsonify, make_response, request
from utils import load, save

app = Flask(__name__)


todos = load()

@app.route('/api/v1/todos', methods=['GET'])
def hello():
	headers = {
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*'
	}
	return make_response((jsonify({'todos': todos}), 200, headers))


@app.route('/api/v1/todos', methods=['POST'])
def addTodo():
	headers = {
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*'
	}
	todo = {
		'id': request.form['id'],
		'title': request.form['title'],
		'done': request.form['done']
	}

	todo['id'] = todos[-1]['id'] + 1

	todos.append(todo)
	save(todos)

	res = {
		'error_code': 0,
		'message': 'add todo successfully'
	}

	return make_response((jsonify(res), 201, headers))


if __name__ == '__main__':
	app.run(debug=True)