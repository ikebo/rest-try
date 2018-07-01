import json
from utils import load, save

with open('todos.txt', encoding='utf-8') as f:
	tds = [
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

	save(tds)
	s = load()
	print(s[0])
