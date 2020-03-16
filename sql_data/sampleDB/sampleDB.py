import sys

sys.path.append('magnus/sql_data/')

from db_operations import db_operations

# should be global based on moment circumstances
global PATH
PATH = "magnus/sql_data/"

class sampleDB():

	def __init__(self):
		super(sampleDB, self).__init__()

	id = "id"
	name = "name"
	programming_language = "programming_language"
	license = "license"
	status = "status"

	dataset = [
		{id: 1, name: "magnus", programming_language: "Python3", license: "MIT", status: "stable"},
		{id: 2, name: "misha", programming_language: "Python3", license: "MIT", status: "stable"},
		{id: 3, name: "esential", programming_language: "C++17", license: "MIT", status: "stable"},
		{id: 4, name: "easyPass", programming_language: "C++17", license: "MIT", status: "stable"},
		{id: 5, name: "easyPass-WS", programming_language: "C++17", license: "MIT", status: "stable"},
		{id: 6, name: "clean-systems", programming_language: "C++17", license: "MIT", status: "stable"},
		{id: 7, name: "cpp-algo-data-structures", programming_language: "C++17", license: "MIT", status: "stable"},
		{id: 8, name: "c-algo-data-structures", programming_language: "C", license: "MIT", status: "stable"},
		{id: 9, name: "clean-TDD", programming_language: "C", license: "MIT", status: "stable"},
		{id: 10, name: "cosmo", programming_language: "Swift", license: "MIT", status: "stable"},
		{id: 11, name: "doppler", programming_language: "JavaScript", license: "MIT", status: "stable"},
		{id: 12, name: "data-analysis-systems", programming_language: "Jupyter Notebook", license: "MIT", status: "stable"},
		{id: 13, name: "rock-paper-scissors-lizard-spock", programming_language: "Java", license: "Apache License 2.0", status: "stable"},
		{id: 14, name: "X-and-0-game", programming_language: "CSharp", license: "Apache License 2.0", status: "stable"},
		{id: 15, name: "csharp-algo-data-structures", programming_language: "CSharp", license: "MIT", status: "stable"},
		{id: 16, name: "smart-code-notes", programming_language: "None", license: "MIT", status: "in progress"},
	]

db_actions = db_operations()


print("\nC projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "C")

print("\nC++17 projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "C++17")

print("\nCSharp projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "CSharp")

print("\nJava projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "Java")

print("\nPython3 projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "Python3")

print("\nJupyter Notebook projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "Jupyter Notebook")

print("\nJavaScript projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "JavaScript")

print("\nSwift projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "Swift")

db_actions.insert_table_in_file(PATH + "/sampleDB/saved_data/programming_languages_classification.data", sampleDB)

db_actions.save_activity("sampleDB", "sampleDB")
