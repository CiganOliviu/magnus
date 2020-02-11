import sys

sys.path.append('magnus/sql_data/')

from db_operations import db_operations

class sampleDB():

	def __init__(self):
		super(sampleDB, self).__init__()

	id = "id"
	name = "name"
	programming_language = "programming_language"
	license = "license"
	
	dataset = [
		{id: 1, name: "magnus", programming_language: "Python3", license: "MIT"},
		{id: 2, name: "misha", programming_language: "Python3", license: "MIT"},
		{id: 3, name: "esential", programming_language: "C++17", license: "MIT"},
		{id: 4, name: "easyPass", programming_language: "C++17", license: "MIT"},
		{id: 5, name: "easyPass-WS", programming_language: "C++17", license: "MIT"},
		{id: 6, name: "clean-systems", programming_language: "C++17", license: "MIT"},
		{id: 7, name: "algo-data-structures", programming_language: "C++17", license: "MIT"},
	]

db_actions = db_operations()

db_actions.describe(sampleDB)
db_actions.save_activity("sampleDB")
