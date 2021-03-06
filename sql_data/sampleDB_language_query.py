from db_operations import db_operations
from sampleDB.sampleDB import sampleDB

DATA_FILE_PATH = "/media/cigan/Personal/Projects/magnus/sql_data/sampleDB/saved_data/programming_languages_classification.data"
JSON_DATA_FILE_PATH = "/media/cigan/Personal/Projects/magnus/sql_data/sampleDB/saved_data/programming_languages_classification_json.data"
SAVE_ACTIVITY_FILE_PATH = "/media/cigan/Personal/Projects/magnus/sql_data/sampleDB"

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

print("\nGo projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "Go")

print("\nKotlin projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "Kotlin")

print("\nCSS projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "CSS")

print("\nHTML projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "HTML")

print("\nDart projects")
db_actions.select_specific_data(sampleDB, sampleDB.programming_language, "Dart")

db_actions.insert_table_in_file(DATA_FILE_PATH, sampleDB)

db_actions.insert_data_in_file(JSON_DATA_FILE_PATH, sampleDB)

db_actions.save_activity(SAVE_ACTIVITY_FILE_PATH, "sampleDB")
