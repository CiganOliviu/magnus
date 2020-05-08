from db_operations import db_operations
from books.books import books

PATH = "magnus/sql_data/"

db_actions = db_operations()

db_actions.select_from_table(books)

db_actions.insert_table_in_file("", books)

db_actions.save_activity("", "books")
