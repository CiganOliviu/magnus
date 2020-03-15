import sys

sys.path.append('magnus/sql_data/')

from db_operations import db_operations

# should be global based on moment circumstances

global PATH
PATH = 'magnus/sql_data/'

class toReadBooks():

	def __init__(self):
		super(toReadBooks, self).__init__()

	id = "id"
	book_title = "title"
	author = "author"
	want_level = "want level"

	dataset = [
		{id: 1, book_title: "Think Again", author: "Walter Sinnott-Armstrong", want_level: 10},
		{id: 2, book_title: "Think and Grow Rich", author: "Napoleon Hill", want_level: 8},
		{id: 3, book_title: "The Underdog Advantage", author: "Dean Graziosi", want_level: 7},
		{id: 4, book_title: "The subtle art of not giving a fuck", author: "Mark Manson", want_level: 6},
		{id: 5, book_title: "The power of now", author: "Eckhart Tolle", want_level: 5},
		{id: 6, book_title: "The millionaire real estate investor", author: "Gary Keller", want_level: 4},
		{id: 7, book_title: "The Handbook evolutionary psichology", author: "David Buss", want_level: 7},
		{id: 8, book_title: "The Clean Coder", author: "Robert C. Martin", want_level: 10},
		{id: 9, book_title: "Rental Property Investing", author: "Brandon Turner", want_level: 4},
		{id: 10, book_title: "The 80/20 rule", author: "Richard Koch", want_level: 7},
		{id: 11, book_title: "The 4-hour workweek", author: "Timothy Ferriss", want_level: 7},
		{id: 12, book_title: "Start with why", author: "Simon Sinek", want_level: 9},
		{id: 13, book_title: "Smart Thinking", author: "Matthew Allen", want_level: 10},
		{id: 14, book_title: "The rules of work", author: "Richard Templar", want_level: 9},
		{id: 15, book_title: "Rich Dad Poor Dad", author: "Robert T. Kiyosaki", want_level: 8},
		{id: 16, book_title: "So good they can't ignore you", author: "Cal Newport", want_level: 9},
		{id: 17, book_title: "Mindset", author: "Dr Carol S. Dweck", want_level: 7},
		{id: 18, book_title: "Dark psichology to manipulate and control people", author: "Arthur Horn", want_level: 9},
		{id: 19, book_title: "Introduction to machine learning with Python", author: "Andreas C. Muller and Sarah Guido", want_level: 5},
		{id: 20, book_title: "How to invest in real estate", author: "Robert Waller", want_level: 5},
		{id: 21, book_title: "Exactly what to say", author: "Phil M. Jones", want_level: 6},
		{id: 22, book_title: "Everything is fucked", author: "Mark Manson", want_level: 8},
		{id: 23, book_title: "Elon Musk", author: "Ashlee Vance", want_level: 8},
		{id: 24, book_title: "Ego is the enemy", author: "Ryan Holiday", want_level: 7},
		{id: 25, book_title: "Dark psichology", author: "Richard Campbell", want_level: 6},
		{id: 26, book_title: "Why We Sleep", author: "Matthew Walker", want_level: 9},
		{id: 27, book_title: "24 Patterns for Clean Code", author: "Robert Beisert", want_level: 10},
		{id: 28, book_title: "Clean Arhitecture", author: "Robert C. Martin", want_level: 10},
	]

db_actions = db_operations()

db_actions.select_from_table(toReadBooks)
db_actions.insert_data_in_file(PATH + "/books/saved_data/toReadBooks.data", toReadBooks)
db_actions.save_activity("books", "toReadBooks")
