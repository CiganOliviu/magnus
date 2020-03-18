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
	status = "status"

	dataset = [
		{id: 1, book_title: "Think Again", author: "Walter Sinnott-Armstrong", want_level: 10, status: "owned"},
		{id: 2, book_title: "Think and Grow Rich", author: "Napoleon Hill", want_level: 8, status: "owned"},
		{id: 3, book_title: "The Underdog Advantage", author: "Dean Graziosi", want_level: 7, status: "owned"},
		{id: 4, book_title: "The subtle art of not giving a fuck", author: "Mark Manson", want_level: 6, status: "owned"},
		{id: 5, book_title: "The power of now", author: "Eckhart Tolle", want_level: 5, status: "owned"},
		{id: 6, book_title: "The millionaire real estate investor", author: "Gary Keller", want_level: 4, status: "owned"},
		{id: 7, book_title: "The Handbook evolutionary psichology", author: "David Buss", want_level: 7, status: "owned"},
		{id: 8, book_title: "The Clean Coder", author: "Robert C. Martin", want_level: 10, status: "owned"},
		{id: 9, book_title: "Rental Property Investing", author: "Brandon Turner", want_level: 4, status: "owned"},
		{id: 10, book_title: "The 80/20 rule", author: "Richard Koch", want_level: 7, status: "owned"},
		{id: 11, book_title: "The 4-hour workweek", author: "Timothy Ferriss", want_level: 7, status: "owned"},
		{id: 12, book_title: "Start with why", author: "Simon Sinek", want_level: 9, status: "owned"},
		{id: 13, book_title: "Smart Thinking", author: "Matthew Allen", want_level: 10, status: "owned"},
		{id: 14, book_title: "The rules of work", author: "Richard Templar", want_level: 9, status: "owned"},
		{id: 15, book_title: "Rich Dad Poor Dad", author: "Robert T. Kiyosaki", want_level: 8, status: "owned"},
		{id: 16, book_title: "So good they can't ignore you", author: "Cal Newport", want_level: 9, status: "owned"},
		{id: 17, book_title: "Mindset", author: "Dr Carol S. Dweck", want_level: 7, status: "owned"},
		{id: 18, book_title: "Dark psichology to manipulate and control people", author: "Arthur Horn", want_level: 9, status: "owned"},
		{id: 19, book_title: "Introduction to machine learning with Python", author: "Andreas C. Muller and Sarah Guido", want_level: 5, status: "owned"},
		{id: 20, book_title: "How to invest in real estate", author: "Robert Waller", want_level: 5, status: "owned"},
		{id: 21, book_title: "Exactly what to say", author: "Phil M. Jones", want_level: 6, status: "owned"},
		{id: 22, book_title: "Everything is fucked", author: "Mark Manson", want_level: 8, status: "owned"},
		{id: 23, book_title: "Elon Musk", author: "Ashlee Vance", want_level: 8, status: "owned"},
		{id: 24, book_title: "Ego is the enemy", author: "Ryan Holiday", want_level: 7, status: "owned"},
		{id: 25, book_title: "Dark psichology", author: "Richard Campbell", want_level: 6, status: "owned"},
		{id: 26, book_title: "Why We Sleep", author: "Matthew Walker", want_level: 9, status: "owned"},
		{id: 28, book_title: "Clean Arhitecture", author: "Robert C. Martin", want_level: 10, status: "owned"},
		{id: 29, book_title: "Code Complete: A Practical Handbook of Software Construction: ", author: "Steve McConnell", want_level: 10, status: "owned"},
		{id: 30, book_title: "Structure and Interpretation of Computer Programs, 2nd Edition (MIT Electrical Engineering and Computer Science)", author: "Harold Abelso", want_level: 10, status: "owned"},
		{id: 31, book_title: "Design patterns : elements of reusable object-oriented software", author: "Erich Gamma", want_level: 10, status: "owned"},
		{id: 32, book_title: "Head First Design Patterns", author: "Eric Freeman", want_level: 10, status: "owned"},
		{id: 33, book_title: "Refactoring: Improving the Design of Existing Code (Object Technology Series)", author: "Kent Beck", want_level: 10, status: "owned"},
		{id: 34, book_title: "Working Effectively with Legacy Code", author: "Michael Feathers", want_level: 10, status: "not-owned"},
		{id: 35, book_title: "The Art of Computer Programming, Volumes 1-4A Boxed Set (Box Set)", author: "Donald E. Knuth", want_level: 10, status: "owned"},
		{id: 36, book_title: "Compilers: Principles, Techniques, and Tools", author: "Alfred V. Aho", want_level: 10, status: "owned"},
		{id: 37, book_title: "The Complete Software Developer's Career Guide: How to Learn Programming Languages Quickly, Ace Your Programming Interview, and Land Your Software Developer Dream Job", author: "John Sonmez", want_level: 10, status: "owned"},
		{id: 38, book_title: "The Pragmatic Programmer: From Journeyman to Master", author: "Andrew Hunt", want_level: 10, status: "owned"},
		{id: 39, book_title: "The Passionate Programmer: Creating a Remarkable Career in Software Development (Pragmatic Life)", author: "Chad Fowler", want_level: 10, status: "owned"},
		{id: 40, book_title: "The Mythical Man-Month: Essays on Software Engineering, Anniversary Edition", author: "Frederick P. Brooks Jr.", want_level: 10, status: "owned"},
		{id: 41, book_title: "Domain-Driven Design: Tackling Complexity in the Heart of Software", author: "Eric Evans", want_level: 10, status: "owned"},
		{id: 42, book_title: "Patterns of Enterprise Application Architecture (The Addison-Wesley Signature Series)", author: "Martin Fowler", want_level: 10, status: "owned"},
		{id: 43, book_title: "Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions (Addison-Wesley Signature Series (Fowler))", author: "Gregor Hohpe", want_level: 10, status: "owned"},
		{id: 44, book_title: "Refactoring to Patterns (Addison-Wesley Signature)", author: "Joshua Kerievsky", want_level: 10, status: "not-owned"},
		{id: 45, book_title: "Agile Software Development, Principles, Patterns, and Practices", author: "Robert C. Martin", want_level: 10, status: "owned"},
		{id: 46, book_title: "Agile Principles, Patterns, and Practices in C#", author: "Robert C. Martin", want_level: 10, status: "owned"},
		{id: 47, book_title: "Agile Estimating and Planning", author: "Robert C, Martin", want_level: 10, status: "not-owned"},
		{id: 48, book_title: "User Stories Applied: For Agile Software Development (Addison-Wesley Signature)", author: "Mike Cohn", want_level: 10, status: "not-owned"},
		{id: 49, book_title: "Extreme Programming Explained: Embrace Change", author: "Kent Beck", want_level: 10, status: "not-owned"},
		{id: 50, book_title: "Programming Pearls (ACM Press)", author: "Jon Bentley", want_level: 10, status: "owned"},
		{id: 51, book_title: "Cracking the Coding Interview: 150 Programming Questions and Solutions", author: "Gayle Laakmann McDowell", want_level: 10, status: "owned"},
		{id: 52, book_title: "Thinking in Java, Fourth Edition", author: "Bruce Eckel", want_level: 10, status: "owned"},
		{id: 53, book_title: "Seven Languages in Seven Weeks: A Pragmatic Guide to Learning Programming Languages (Pragmatic Programmers)", author: "Bruce A. Tate", want_level: 10, status: "owned"},
		{id: 54, book_title: "C# in Depth", author: "Jon Skeet", want_level: 10, status: "owned"},
		{id: 55, book_title: "Testing Computer Software", author: "Cem Kaner", want_level: 10, status: "not-owned"},
		{id: 56, book_title: "Ship it!: A Practical Guide to Successful Software Projects (Pragmatic Programmers)", author: "Jared Richardson", want_level: 10, status: "owned"},
		{id: 57, book_title: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Addison-Wesley Signature)", author: "Jez Humble", want_level: 10, status: "owned"},
		{id: 58, book_title: "Soft Skills: The software developer's life manual", author: "John Sonmez", want_level: 10, status: "owned"},
		{id: 59, book_title: "Code: The Hidden Language of Computer Hardware and Software", author: "Charles Petzold", want_level: 10, status: "owned"},
		{id: 60, book_title: "Godel, Escher, Bach: An Eternal Golden Braid", author: "Douglas R. Hofstadter", want_level: 10, status: "not-owned"},
		{id: 61, book_title: "The War of Art", author: "Steven Pressfield", want_level: 10, status: "not-owned"},
		{id: 62, book_title: "As a Man Thinketh", author: "James Allen", want_level: 10, status: "not-owned"},
		{id: 63, book_title: "Maximum Achievement: Strategies and Skills That Will Unlock Your Hidden Powers to Succeed", author: "Brian Tracy", want_level: 10, status: "not-owned"},
		{id: 64, book_title: "How to Fail at Almost Everything and Still Win Big: Kind of the Story of My Life", author: "Scott Adams", want_level: 10, status: "not-owned"},
		{id: 65, book_title: "The Obstacle Is the Way: The Timeless Art of Turning Trials into Triumph", author: "Ryan Holiday", want_level: 10, status: "not-owned"},
		{id: 66, book_title: "Panzer Leader", author: "Heinz Guaderian", want_level: 10, status: "owned"},
		{id: 67, book_title: "Operation Barbarossa 2nd Panzergruppe in Russia June 21 1941", author: "Heinz Guaderian", want_level: 10, status: "owned"},
		{id: 68, book_title: "Sleep Smarter", author: "Shawn Stevenson", want_level: 8, status: "not-owned"},
	]

db_actions = db_operations()

db_actions.describe(toReadBooks)

db_actions.insert_table_in_file(PATH + "/books/saved_data/toReadBooks.data", toReadBooks)

db_actions.save_activity("books/logfiles/", "toReadBooks")
