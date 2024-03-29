class books():

	def __init__(self):
		super(books, self).__init__()

	id = "id"
	book_title = "title"
	author = "author"

	dataset = [
		{id: 1, book_title: "Destined to win", author: "Alex Uwejeh"},
		{id: 2, book_title: "Secret to help boost self confidence", author: "Peter Abeland"},
		{id: 3, book_title: "Ideas", author: "Tonoy Egar"},
		{id: 4, book_title: "Productivity NINJA", author: "Graham Allcot"},
		{id: 5, book_title: "DevOps Hiring", author: "Dave Swiebacl"},
		{id: 6, book_title: "Nikola Tesla", author: "Sean Patrick"},
		{id: 7, book_title: "Disruptive possibilities", author: "Jeffey Needham"},
		{id: 8, book_title: "What is SEO ?", author: "Dan Kerns"},
		{id: 9, book_title: "UX Design", author: "Soumen Das"},
		{id: 10, book_title: "Analyzing the Analyzers", author: "Harlan Harris"},
		{id: 11, book_title: "The evolution of Data Production", author: "Mike Loukides"},
		{id: 12, book_title: "Day Trading Secrets", author: "Harvey Walsh"},
		{id: 13, book_title: "Real-Time Big Data", author: "Mike Barlow"},
		{id: 14, book_title: "Motivation for success", author: "Larry Freeman"},
		{id: 15, book_title: "5 Steps to a stress free retirement", author: "Steve Hoover"},
		{id: 16, book_title: "How to relax", author: "Martin Meadowns"},
		{id: 17, book_title: "Confidence", author: "Martin Meadowns"},
		{id: 18, book_title: "Economy Impact", author: "Mike Hendrickson"},
		{id: 19, book_title: "What is NODE", author: "Brett McLaughlin"},
		{id: 20, book_title: "What is Data Science", author: "Mike Loukides"},
		{id: 21, book_title: "How to think bigger", author: "Martin Meadowns"},
		{id: 22, book_title: "Planning your business success", author: "Steve Hoover"},
		{id: 23, book_title: "Open Source Strategies", author: "Simon Philipps"},
		{id: 24, book_title: "Algorimti fundamentali", author: "Mirel Cosulschi"},
		{id: 25, book_title: "Rework", author: "Jason Fried"},
		{id: 26, book_title: "Mein Kampf", author: "Adolf Hitler"},
		{id: 27, book_title: "A Tree Grows in Brooklyn", author: "Betty Smith"},
		{id: 28, book_title: "The Devil's Arithmetic", author: "Jane Yolen"},
		
		{id: 29, book_title: "It's Kind of a Funny Story", author: "Ned Vizzini"},
		{id: 30, book_title: "Arctic Adventure", author: "Peter Freunchen"},
		{id: 31, book_title: "Metode de programare si POO", author: "Eugen Popescu"},
		{id: 32, book_title: "How to win friends and influence people", author: "Dale Carnegie"},
		{id: 33, book_title: "Python Pocket Refferenece", author: "Lutz"},
		{id: 34, book_title: "Ajax", author: "Phill Ballard"},
		{id: 35, book_title: "Java in easy steps", author: "Mike McGrath"},
		{id: 36, book_title: "Java from 0 to expert", author: "Stefan Tanase"},
		{id: 37, book_title: "Totul despre C si C++", author: "Lars Kandler"},
		{id: 38, book_title: "Manualul tau de PHP", author: "Traian Anghel"},
		{id: 39, book_title: "UNIX Procese", author: "Iosif Ignat"},
		{id: 40, book_title: "Ingineria sistemelor soft", author: "Dorin Bocu"},
		{id: 41, book_title: "JavaScript", author: "Alina Caltan"},
		{id: 42, book_title: "Algoritmi de sortare", author: "Ciprian Ghise"},
		{id: 43, book_title: "Algorimti de optimizare grafuri", author: "Ciprian Ghise"},
		{id: 44, book_title: "20.000 de leghe sub marii", author: "Jules Verne"},
		{id: 45, book_title: "Life 3.0", author: "Max Tegmark"},
		{id: 46, book_title: "The millionaire booklet", author: "Grant Cardone"},
		{id: 47, book_title: "The 10x rule", author: "Grant Cardone"},
		{id: 48, book_title: "Martin cel avid", author: "Willian Golding"},
		{id: 49, book_title: "Millionaire Success Habits", author: "Dean Graziosi"},
		{id: 50, book_title: "The free-time formula", author: "Jeff Sanders"},
		{id: 51, book_title: "The leader habit", author: "Martin Lanik"},
		{id: 52, book_title: "Written in history", author: "Simon Sebag Montefiore"},
		{id: 53, book_title: "The millionaire dropout", author: "Vince Stanzione"},
		{id: 54, book_title: "Deep work", author: "Cal Newport"},
		{id: 55, book_title: "The surprising science of mettings", author: "SG Rogelberg"},
		{id: 56, book_title: "We're all marketers", author: "Nico De Bruyn"},
		{id: 57, book_title: "Think like a billionaire", author: "Donald Trump"},
		{id: 58, book_title: "How to skimm your life", author: "The Skimm"},
		{id: 59, book_title: "Millionaire Success Habits: Productivity Chapters", author: "Dean Graziosi"},
		{id: 60, book_title: "Chernobyl", author: "Serhoo Plokhy"},
		{id: 61, book_title: "The Coffe bean", author: "Jon Gordon, Damon West"},
		{id: 62, book_title: "Steal the show", author: "Michael Port"},
		{id: 63, book_title: "Clean Code", author: "Robert C. Martin"},
		{id: 64, book_title: "The One Thing", author: "Garry Keller"},
		{id: 65, book_title: "Be obsessed or be average", author: "Grant Cardone"},
		{id: 66, book_title: "24 Patterns for Clean Code", author: "Robert Beisert"},
		{id: 67, book_title: "Clean Arhitecture", author: "Robert C. Martin"},
		{id: 68, book_title: "Man alone with himself", author: "R. J. Nietzsche"},
		{id: 69, book_title: "The Clean Coder", author: "Robert C. Martin"},
		{id: 70, book_title: "On the heights of despair", author: "Emil Cioran"},
		{id: 71, book_title: "The art of war", author: "Sun Tzu"},
    	{id: 72, book_title: "Implementation Patterns", author: "Kent Beck"},
		{id: 73, book_title: "God Explained in a Taxi Ride", author: "Paul Arden"},
		{id: 74, book_title: "Damn Good Advices", author: "George Lois"},
		{id: 75, book_title: "Assassin's Creed: The Secret Crusade", author: "Bowden Oliver"},
		{id: 76, book_title: "Un IQ financiar mai bun", author: "Robert Kiyosaki"},
	]
