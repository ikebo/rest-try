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
		'done': False if request.form['done'] == 'false' else True
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



@app.route('/api/v1/todo/<int:editId>', methods=['PUT', 'OPTIONS'])
def editTodo(editId):
	headers = {
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*',
		'Access-Control-Allow-Methods': 'PUT'
	}
	 	
	if request.method == 'OPTIONS':
		return make_response((jsonify({'message': 'come on!'}), 202, headers))

	todo = {
		'id': editId,
		'title': request.form['title'],
		'done': False if request.form['done'] == 'false' else True
	}

	error_code = 0
	message = 'edit todo with id ' + str(editId) + ' successfully'

	for index, xtodo in enumerate(todos):
		if xtodo['id'] == editId:
			xtodo['title'] = todo['title']
			xtodo['done'] = todo['done']
			todos[index] = xtodo
			break
	else:
		error_code = 1
		message = 'edit todo with id ' + str(editId) + ' failed'

	save(todos)

	res = {
		'error_code': error_code,
		'message': message
	}

	return make_response((jsonify(todo), 202, headers))



if __name__ == '__main__':
	app.run(debug=True)