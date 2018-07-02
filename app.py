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


@app.route('/api/v1/todos/<int:delId>', methods=['DELETE', 'OPTIONS'])
def deleteTodo(delId):
	headers = {
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*',
		'Access-Control-Allow-Methods': 'DELETE'
	}
  	
	if request.method == 'OPTIONS':
		return make_response((jsonify({'message': 'come on!'}), 202, headers))


	error_code = 0
	message = 'delete todo with id ' + str(delId) + ' successfully'

	for todo in todos:
		if todo['id'] == delId:
  			todos.remove(todo)
  			break
	else:
  		error_code = 1
  		message = 'delete todo with id ' + str(delId) + ' failed'

	save(todos)

	res = {
  		'error_code': error_code,
  		'message': message
  	}

	return make_response((jsonify(res), 203, headers))


if __name__ == '__main__':
	app.run(debug=True)