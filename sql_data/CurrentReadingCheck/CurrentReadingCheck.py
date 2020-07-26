class CurrentReadingCheck():

	def __init__(self):
		super(CurrentReadingCheck, self).__init__()

	id = "id"
	book_title = "title"
	author = "author"
	current_page = "current page"

	dataset = [
		{id: 1, book_title: "Refactoring", author: "Martin Flower", current_page: 111},
		{id: 2, book_title: "Soft skills", author: "John Sonmez", current_page: 163},
		{id: 3, book_title: "Lean UX", author: "Jeff Gothelf", current_page: 0},
		{id: 4, book_title: "It doesen't have to be crazy at work", author: "Jason Fried", current_page: 0},
		{id: 5, book_title: "How to sleep well", author: "Neil Stanley", current_page: 0},
		{id: 6, book_title: "The trouble with being born", author: "Emil Cioran", current_page: 32},
		{id: 7, book_title: "Every man dies alone", author: "Hans Fallada", current_page: 0},
		{id: 8, book_title: "God Explained in a Taxi Ride", author: "Paul Arden", current_page: 0},
		{id: 9, book_title: "Damn good advice", author: "George Lois", current_page: 55},
	]
