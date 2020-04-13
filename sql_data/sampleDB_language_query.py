from db_operations import db_operations
from sampleDB.sampleDB import sampleDB

PATH = "magnus/sql_data/"

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

print("\nPHP projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "PHP")

print("\nRust projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "Rust")

db_actions.insert_table_in_file(PATH + "/sampleDB/saved_data/programming_languages_classification.data", sampleDB)

db_actions.save_activity(PATH + "sampleDB", "sampleDB")