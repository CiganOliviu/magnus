from db_operations import db_operations
from books.toReadBooks import toReadBooks

PATH = "magnus/sql_data/"

db_actions = db_operations()

db_actions.describe(toReadBooks)

db_actions.insert_table_in_file("", toReadBooks)

db_actions.save_activity("", "toReadBooks")
