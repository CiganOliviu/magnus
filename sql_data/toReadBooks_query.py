from db_operations import db_operations
from books.toReadBooks import toReadBooks

DATA_FILE_PATH = "\magnus\sql_data\\books\saved_data\\to_read_books\\toReadBooks.data"
JSON_DATA_FILE_PATH = "\magnus\sql_data\\books\saved_data\\to_read_books\\toReadBooks_json.data"
SAVE_ACTIVITY_FILE_PATH = "\magnus\sql_data\\books\logfiles\\"

db_actions = db_operations()

db_actions.describe(toReadBooks)

db_actions.insert_table_in_file(DATA_FILE_PATH, toReadBooks)

db_actions.insert_data_in_file(JSON_DATA_FILE_PATH, toReadBooks)

db_actions.save_activity(SAVE_ACTIVITY_FILE_PATH, "toReadBooks")
