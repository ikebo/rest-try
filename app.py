from flask import Flask, jsonify, make_response

app = Flask(__name__)


todos = [
	{
		'id': 1,
		'title': '洗衣服',
		'status': False
	},
	{
		'id': 2,
		'title': '做饭',
		'status': False,
	},
	{
		'id': 3,
		'title': '喝水',
		'status': True
	}
]



@app.route('/api/v1/todos', methods=['GET'])
def hello():
	headers = {
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*'
	}
	return make_response((jsonify({'todos': todos}), 200, headers))


if __name__ == '__main__':
	app.run(debug=True)