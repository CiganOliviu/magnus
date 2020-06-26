class CurrentReadingCheck():

	def __init__(self):
		super(CurrentReadingCheck, self).__init__()

    id = "id"
    book_title: "title"
    author: "author"
    current_page: "current page"
    
	dataset = [
		{id: 1, book_title: "Refactoring", author: "Martin Flower", current_page: 100},
		{id: 2, book_title: "Implementation Patterns", author: "Kent Beck", current_page: 143},
    {id: 3, book_title: "Soft skills", author: "John Sonmez", current_page: 163},
	]
