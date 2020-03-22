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
	done_to_read = "done to read"

	dataset = [
		{id: 1, book_title: "Think Again", author: "Walter Sinnott Armstrong", want_level: 10, status: "owned",	done_to_read: False},
		{id: 2, book_title: "Think and Grow Rich", author: "Napoleon Hill", want_level: 8, status: "owned", done_to_read: False},
		{id: 3, book_title: "The Underdog Advantage", author: "Dean Graziosi", want_level: 7, status: "owned", done_to_read: False},
		{id: 4, book_title: "The subtle art of not giving a fuck", author: "Mark Manson", want_level: 6, status: "owned", done_to_read: False},
		{id: 5, book_title: "The power of now", author: "Eckhart Tolle", want_level: 5, status: "owned", done_to_read: False},
		{id: 6, book_title: "The millionaire real estate investor", author: "Gary Keller", want_level: 4, status: "owned", done_to_read: False},
		{id: 7, book_title: "The Handbook evolutionary psichology", author: "David Buss", want_level: 7, status: "owned", done_to_read: False},
		{id: 8, book_title: "The Clean Coder", author: "Robert C. Martin", want_level: 10, status: "owned", done_to_read: False},
		{id: 9, book_title: "Rental Property Investing", author: "Brandon Turner", want_level: 4, status: "owned", done_to_read: False},
		{id: 10, book_title: "The 80/20 rule", author: "Richard Koch", want_level: 7, status: "owned", done_to_read: False},
		{id: 11, book_title: "The 4 hour workweek", author: "Timothy Ferriss", want_level: 7, status: "owned", done_to_read: False},
		{id: 12, book_title: "Start with why", author: "Simon Sinek", want_level: 9, status: "owned", done_to_read: False},
		{id: 13, book_title: "Smart Thinking", author: "Matthew Allen", want_level: 10, status: "owned", done_to_read: False},
		{id: 14, book_title: "The rules of work", author: "Richard Templar", want_level: 9, status: "owned", done_to_read: False},
		{id: 15, book_title: "Rich Dad Poor Dad", author: "Robert T. Kiyosaki", want_level: 8, status: "owned", done_to_read: False},
		{id: 16, book_title: "So good they can't ignore you", author: "Cal Newport", want_level: 9, status: "owned", done_to_read: False},
		{id: 17, book_title: "Mindset", author: "Dr Carol S. Dweck", want_level: 7, status: "owned", done_to_read: False},
		{id: 18, book_title: "Dark psichology to manipulate and control people", author: "Arthur Horn", want_level: 9, status: "owned", done_to_read: False},
		{id: 19, book_title: "Introduction to machine learning with Python", author: "Andreas C. Muller and Sarah Guido", want_level: 5, status: "owned", done_to_read: False},
		{id: 20, book_title: "How to invest in real estate", author: "Robert Waller", want_level: 5, status: "owned", done_to_read: False},
		{id: 21, book_title: "Exactly what to say", author: "Phil M. Jones", want_level: 6, status: "owned", done_to_read: False},
		{id: 22, book_title: "Everything is fucked", author: "Mark Manson", want_level: 8, status: "owned", done_to_read: False},
		{id: 23, book_title: "Elon Musk", author: "Ashlee Vance", want_level: 8, status: "owned", done_to_read: False},
		{id: 24, book_title: "Ego is the enemy", author: "Ryan Holiday", want_level: 7, status: "owned", done_to_read: False},
		{id: 25, book_title: "Dark psichology", author: "Richard Campbell", want_level: 6, status: "owned", done_to_read: False},
		{id: 26, book_title: "Why We Sleep", author: "Matthew Walker", want_level: 9, status: "owned", done_to_read: False},
		{id: 28, book_title: "Clean Arhitecture", author: "Robert C. Martin", want_level: 10, status: "owned", done_to_read: True},
		{id: 29, book_title: "Code Complete: A Practical Handbook of Software Construction: ", author: "Steve McConnell", want_level: 10, status: "owned", done_to_read: False},
		{id: 30, book_title: "Structure and Interpretation of Computer Programs, 2nd Edition (MIT Electrical Engineering and Computer Science)", author: "Harold Abelso", want_level: 10, status: "owned", done_to_read: False},
		{id: 31, book_title: "Design patterns : elements of reusable object oriented software", author: "Erich Gamma", want_level: 10, status: "owned", done_to_read: False},
		{id: 32, book_title: "Head First Design Patterns", author: "Eric Freeman", want_level: 10, status: "owned", done_to_read: False},
		{id: 33, book_title: "Refactoring: Improving the Design of Existing Code (Object Technology Series)", author: "Kent Beck", want_level: 10, status: "owned", done_to_read: False},
		{id: 34, book_title: "Working Effectively with Legacy Code", author: "Michael Feathers", want_level: 10, status: "not owned", done_to_read: False},
		{id: 35, book_title: "The Art of Computer Programming, Volumes 1 4A Boxed Set (Box Set)", author: "Donald E. Knuth", want_level: 10, status: "owned", done_to_read: False},
		{id: 36, book_title: "Compilers: Principles, Techniques, and Tools", author: "Alfred V. Aho", want_level: 10, status: "owned", done_to_read: False},
		{id: 37, book_title: "The Complete Software Developer's Career Guide: How to Learn Programming Languages Quickly, Ace Your Programming Interview, and Land Your Software Developer Dream Job", author: "John Sonmez", want_level: 10, status: "owned", done_to_read: False},
		{id: 38, book_title: "The Pragmatic Programmer: From Journeyman to Master", author: "Andrew Hunt", want_level: 10, status: "owned", done_to_read: False},
		{id: 39, book_title: "The Passionate Programmer: Creating a Remarkable Career in Software Development (Pragmatic Life)", author: "Chad Fowler", want_level: 10, status: "owned", done_to_read: False},
		{id: 40, book_title: "The Mythical Man Month: Essays on Software Engineering, Anniversary Edition", author: "Frederick P. Brooks Jr.", want_level: 10, status: "owned", done_to_read: False},
		{id: 41, book_title: "Domain Driven Design: Tackling Complexity in the Heart of Software", author: "Eric Evans", want_level: 10, status: "owned", done_to_read: False},
		{id: 42, book_title: "Patterns of Enterprise Application Architecture (The Addison Wesley Signature Series)", author: "Martin Fowler", want_level: 10, status: "owned", done_to_read: False},
		{id: 43, book_title: "Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions (Addison Wesley Signature Series (Fowler))", author: "Gregor Hohpe", want_level: 10, status: "owned", done_to_read: False},
		{id: 44, book_title: "Refactoring to Patterns (Addison Wesley Signature)", author: "Joshua Kerievsky", want_level: 10, status: "not owned", done_to_read: False},
		{id: 45, book_title: "Agile Software Development, Principles, Patterns, and Practices", author: "Robert C. Martin", want_level: 10, status: "owned", done_to_read: False},
		{id: 46, book_title: "Agile Principles, Patterns, and Practices in C#", author: "Robert C. Martin", want_level: 10, status: "owned", done_to_read: False},
		{id: 47, book_title: "Agile Estimating and Planning", author: "Robert C, Martin", want_level: 10, status: "not owned", done_to_read: False},
		{id: 48, book_title: "User Stories Applied: For Agile Software Development (Addison Wesley Signature)", author: "Mike Cohn", want_level: 10, status: "not owned", done_to_read: False},
		{id: 49, book_title: "Extreme Programming Explained: Embrace Change", author: "Kent Beck", want_level: 10, status: "not owned", done_to_read: False},
		{id: 50, book_title: "Programming Pearls (ACM Press)", author: "Jon Bentley", want_level: 10, status: "owned", done_to_read: False},
		{id: 51, book_title: "Cracking the Coding Interview: 150 Programming Questions and Solutions", author: "Gayle Laakmann McDowell", want_level: 10, status: "owned", done_to_read: False},
		{id: 52, book_title: "Thinking in Java, Fourth Edition", author: "Bruce Eckel", want_level: 10, status: "owned", done_to_read: False},
		{id: 53, book_title: "Seven Languages in Seven Weeks: A Pragmatic Guide to Learning Programming Languages (Pragmatic Programmers)", author: "Bruce A. Tate", want_level: 10, status: "owned", done_to_read: False},
		{id: 54, book_title: "C# in Depth", author: "Jon Skeet", want_level: 10, status: "owned", done_to_read: False},
		{id: 55, book_title: "Testing Computer Software", author: "Cem Kaner", want_level: 10, status: "not owned", done_to_read: False},
		{id: 56, book_title: "Ship it!: A Practical Guide to Successful Software Projects (Pragmatic Programmers)", author: "Jared Richardson", want_level: 10, status: "owned", done_to_read: False},
		{id: 57, book_title: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Addison Wesley Signature)", author: "Jez Humble", want_level: 10, status: "owned", done_to_read: False},
		{id: 58, book_title: "Soft Skills: The software developer's life manual", author: "John Sonmez", want_level: 10, status: "owned", done_to_read: False},
		{id: 59, book_title: "Code: The Hidden Language of Computer Hardware and Software", author: "Charles Petzold", want_level: 10, status: "owned", done_to_read: False},
		{id: 60, book_title: "Godel, Escher, Bach: An Eternal Golden Braid", author: "Douglas R. Hofstadter", want_level: 10, status: "owned", done_to_read: False},
		{id: 61, book_title: "The War of Art", author: "Steven Pressfield", want_level: 10, status: "owned", done_to_read: False},
		{id: 62, book_title: "As a Man Thinketh", author: "James Allen", want_level: 10, status: "not owned", done_to_read: False},
		{id: 63, book_title: "Maximum Achievement: Strategies and Skills That Will Unlock Your Hidden Powers to Succeed", author: "Brian Tracy", want_level: 10, status: "owned", done_to_read: False},
		{id: 64, book_title: "How to Fail at Almost Everything and Still Win Big: Kind of the Story of My Life", author: "Scott Adams", want_level: 10, status: "owned", done_to_read: False},
		{id: 65, book_title: "The Obstacle Is the Way: The Timeless Art of Turning Trials into Triumph", author: "Ryan Holiday", want_level: 10, status: "owned", done_to_read: False},
		{id: 66, book_title: "Panzer Leader", author: "Heinz Guaderian", want_level: 10, status: "owned", done_to_read: False},
		{id: 67, book_title: "Operation Barbarossa 2nd Panzergruppe in Russia June 21 1941", author: "Heinz Guaderian", want_level: 10, status: "owned", done_to_read: False},
		{id: 68, book_title: "Sleep Smarter", author: "Shawn Stevenson", want_level: 8, status: "not owned", done_to_read: False},
		{id: 69, book_title: "Find Your Why A Practical Guide for Discovering Purpose for You and Your Team", author: "Simon Sinek", want_level: 7, status: "owned", done_to_read: False},
		{id: 70, book_title: "Man alone with himself", author: "Josh Kaufman", want_level: 8, status: "owned", done_to_read: False},
		{id: 71, book_title: "The Personal MBA Master the Art of Business", author: "R. J. Nietzsche", want_level: 10, status: "owned", done_to_read: False},
		{id: 72, book_title: "The Intelligent Investor The Definitive Book On Value Investing, Revised Edition", author: "Benjamin Graham", want_level: 8, status: "owned", done_to_read: False},
		{id: 73, book_title: "Unshakeable Your Financial Freedom Playbook", author: "Tony Robbins", want_level: 8, status: "owned", done_to_read: False},
		{id: 74, book_title: "Students Secrets Revealed", author: "Dean Graziosi", want_level: 8, status: "owned", done_to_read: False},
		{id: 75, book_title: "The Four Pillars of Investing Lessons for Building a Winning Portfolio", author: "William Bernstein", want_level: 10, status: "owned", done_to_read: False},
		{id: 76, book_title: "Speed Reading For Dummies", author: "Richard Sutz", want_level: 10, status: "owned", done_to_read: False},
		{id: 77, book_title: "The H Factor of Personality Why Some People are Manipulative, Self Entitled, Materialistic, and Exploitive And Why It Matters for Everyone", author: "Kibeom Lee", want_level: 8, status: "owned", done_to_read: False},
		{id: 78, book_title: "Built to Sell Creating a Business That Can Thrive Without You", author: "John Warrillow", want_level: 9, status: "owned", done_to_read: False},
		{id: 79, book_title: "Rich Dads Guide to Investing What the Rich Invest in That the Poor and Middle Class Do Not", author: " Robert T. Kiyosaki", want_level: 8, status: "owned", done_to_read: False},
		{id: 80, book_title: "Passive Income Stop Working   Start Living   Make money while you sleep", author: "Ralph Waters", want_level: 10, status: "owned", done_to_read: False},
		{id: 81, book_title: "The Freelancers Bible Everything You Need to Know to Have the Career of Your Dreams   On Your Terms", author: "Sara Horowitz", want_level: 10, status: "owned", done_to_read: False},
		{id: 82, book_title: "The Selfish Gene", author: "Richard Dawkins", want_level: 8, status: "owned", done_to_read: False},
		{id: 83, book_title: "How to Analyze People   Dark Secrets to Analyze and Influence Anyone Using Body Language ", author: "James Williams", want_level: 6, status: "owned", done_to_read: False},
		{id: 84, book_title: "No One Understands You and What to Do About It", author: "Heidi Grant Halvorson", want_level: 6, status: "owned", done_to_read: False},
		{id: 85, book_title: "The Greatest Minds and Ideas of All Time", author: "Will Durant", want_level: 10, status: "owned", done_to_read: False},
		{id: 86, book_title: "Purple Cow Transform Your Business by Being Remarkable", author: "Seth Godin", want_level: 8, status: "owned", done_to_read: False},
		{id: 87, book_title: "A Night to Remember The Classic Bestselling Account of the Sinking of the Titanic", author: "Walter Lord", want_level: 8, status: "owned", done_to_read: False},
		{id: 88, book_title: "Business Adventures Twelve Classic Tales from the World of Wall Street", author: "John Brooks", want_level: 7, status: "owned", done_to_read: False},
		{id: 89, book_title: "Why We Buy The Science of Shopping  Updated and Revised for the Internet, the Global Consumer, and Beyond", author: "Paco Underhill", want_level: 8, status: "owned", done_to_read: False},
		{id: 90, book_title: "Activate Your Brain How Understanding Your Brain Can Improve Your Work   and Your Life", author: "Scott G. Halford", want_level: 8, status: "owned", done_to_read: False},
		{id: 91, book_title: "Listen out loud  a life in music  managing McCartney, Madonna, and Michael Jackson", author: "Weisner", want_level: 7, status: "owned", done_to_read: False},
		{id: 92, book_title: "The Art of Creative Thinking How to Be Innovative and Develop Great Ideas", author: "John Adair", want_level: 8, status: "owned", done_to_read: False},
		{id: 93, book_title: "Focus use different ways of seeing the world for success and influence", author: "Heidi Grant Halvorson", want_level: 10, status: "owned", done_to_read: False},
		{id: 94, book_title: "Leadership Secrets of the Worlds Most Successful CEOs 100 Top Executives Reveal the Management Strategies That Made Their Companies Great", author: "Eric Yaverbaum", want_level: 10, status: "owned", done_to_read: False},
		{id: 95, book_title: "Managing Oneself", author: "Peter Ferdinand Drucker", want_level: 10, status: "owned", done_to_read: False},
		{id: 96, book_title: "The Richest Man in Babylon", author: "George S. Clason", want_level: 10, status: "owned", done_to_read: False},
		{id: 97, book_title: "You Are a Badass How to Stop Doubting Your Greatness and Start Living an Awesome Life", author: "Jen Sincero", want_level: 10, status: "owned", done_to_read: False},
		{id: 98, book_title: "The Art of War", author: "Sun Tzu", want_level: 10, status: "owned", done_to_read: False},
		{id: 99, book_title: "Grit The Power of Passion and Perseverance", author: "Angela Duckworth", want_level: 8, status: "owned", done_to_read: False},
		{id: 100, book_title: "Book Yourself Solid The Fastest, Easiest, and Most Reliable System for Getting More Clients Than You Can Handle Even if You Hate Marketing and Selling", author: "Michael Port", want_level: 10, status: "owned", done_to_read: False},
		{id: 101, book_title: "Tested Advertising Methods", author: "John Caples", want_level: 10, status: "owned", done_to_read: False},
		{id: 102, book_title: "The Winner Effect The Neuroscience of Success and Failure", author: "Ian H. Robertson", want_level: 10, status: "owned", done_to_read: False},
		{id: 103, book_title: "Creative Cash Flow Reporting Uncovering Sustainable Financial Performance", author: "Charles W. Mulford", want_level: 10, status: "owned", done_to_read: False},
		{id: 104, book_title: "Rich Dads Increase Your Financial IQ Get Smarter with Your Money", author: "Robert T. Kiyosaki", want_level: 10, status: "owned", done_to_read: False},
		{id: 105, book_title: "The Courage to be Disliked How to Change Your Life and Achieve Real Happiness ", author: "Ichiro Kishimi Fumitake Koga", want_level: 10, status: "owned", done_to_read: False},
		{id: 106, book_title: "The Wealth Paradox Economic Prosperity and the Hardening of Attitudes", author: "Frank Mols", want_level: 10, status: "owned", done_to_read: False},
		{id: 107, book_title: "The Financial Rules for New College Graduates Invest before Paying Off Debt and Other Tips Your Professors Didn’t Teach You", author: "Michael C Taylor", want_level: 10, status: "owned", done_to_read: False},
		{id: 108, book_title: "The Millionaire Next Door The Surprising Secrets of Americas Wealthy", author: "Thomas J. Stanley", want_level: 10, status: "owned", done_to_read: False},
	]

db_actions = db_operations()

db_actions.describe(toReadBooks)

db_actions.insert_table_in_file(PATH + "/books/saved_data/toReadBooks.data", toReadBooks)

db_actions.save_activity("books/logfiles/", "toReadBooks")
