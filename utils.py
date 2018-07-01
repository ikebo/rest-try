import json

def load():
	with open('todos.txt', 'r', encoding='utf-8') as f:
		s =  f.read()
		return json.loads(s)


def save(data):
	s = json.dumps(data, indent=2, ensure_ascii=False)
	with open('todos.txt', 'w', encoding='utf-8') as f:
		f.write(s)
