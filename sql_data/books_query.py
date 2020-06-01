from db_operations import db_operations
from books.books import books

DATA_FILE_PATH = "\\magnus\sql_data\\books\saved_data\\books\\books.data"
JSON_DATA_FILE_PATH = "\\magnus\sql_data\\books\saved_data\\books\\books_json.data"
SAVE_ACTIVITY_FILE_PATH = "\\magnus\sql_data\\books\logfiles\\"

db_actions = db_operations()

db_actions.select_from_table(books)

db_actions.insert_table_in_file(DATA_FILE_PATH, books)

db_actions.insert_data_in_file(JSON_DATA_FILE_PATH, books)

db_actions.save_activity(SAVE_ACTIVITY_FILE_PATH, "books")
