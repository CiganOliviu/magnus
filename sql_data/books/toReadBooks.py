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
		{id: 8, book_title: "The Clean Coder", author: "Robert C. Martin", want_level: 10, status: "owned", done_to_read: True},
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
		{id: 70, book_title: "Man alone with himself", author: "R. J. Nietzsche", want_level: 8, status: "owned", done_to_read: True},
		{id: 71, book_title: "The Personal MBA Master the Art of Business", author: "Josh Kaufman", want_level: 10, status: "owned", done_to_read: False},
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
		{id: 109, book_title: "The folly of fools  the logic of deceit and self-deception in human life", author: "Trivers", want_level: 6, status: "owned", done_to_read: False},
		{id: 110, book_title: "Principles of Marketing", author: "Philip T. Kotler", want_level: 7, status: "owned", done_to_read: False},
		{id: 111, book_title: "This Is Marketing You Can’t Be Seen Until You Learn to See", author: "Seth Godin", want_level: 6, status: "owned", done_to_read: False},
		{id: 112, book_title: "The Splendid and the Vile", author: "Erik Larson", want_level: 9, status: "owned", done_to_read: False},
		{id: 113, book_title: "The ANSI C Programming Language", author: "Dennis M. Ritchie", want_level: 10, status: "owned", done_to_read: False},
		{id: 114, book_title: "The C++ Programming Language, 4th Edition", author: "Stroustrup B.", want_level: 9, status: "owned", done_to_read: False},
		{id: 115, book_title: "Fluent Python", author: "Luciano Ramalho", want_level: 9, status: "owned", done_to_read: False},
		{id: 116, book_title: "The Book on Tax Strategies for the Savvy Real Estate Investor Powerful techniques anyone can use to deduct more, invest smarter, and pay far less to the IRS", author: "Amanda Han", want_level: 9, status: "owned", done_to_read: False},
		{id: 117, book_title: "The Book on Flipping Houses How to Buy, Rehab, and Resell Residential Properties", author: "J. Scott", want_level: 10, status: "owned", done_to_read: False},
		{id: 118, book_title: "Disrupt You Master Personal Transformation, Seize Opportunity, and Thrive in the Era of Endless Innovation", author: "Jay Samit", want_level: 9, status: "owned", done_to_read: False},
		{id: 119, book_title: "You Are a Badass at Making Money Master the Mindset of Wealth", author: "Jen Sincero", want_level: 10, status: "owned", done_to_read: False},
		{id: 120, book_title: "Finish What You Start The Art of Following Through, Taking Action, Executing,  Self-Discipline", author: "Peter Hollins", want_level: 10, status: "owned", done_to_read: False},
		{id: 121, book_title: "The Happiness Advantage The Seven Principles of Positive Psychology That Fuel Success and Performance at Work", author: "Shawn Achor", want_level: 7, status: "owned", done_to_read: False},
		{id: 122, book_title: "I Will Teach You to Be Rich, Second Edition No Guilt. No Excuses. No BS. Just a 6-Week Program That Works", author: "Ramit Sethi", want_level: 8, status: "owned", done_to_read: False},
		{id: 123, book_title: "The Social Skills Guidebook Manage Shyness, Improve Your Conversations, and Make Friends, Without Giving Up Who You Are", author: "Chris MacLeod", want_level: 6, status: "owned", done_to_read: False},
		{id: 124, book_title: "The Power of Creativity (Book 1) Learning How to Build Lasting Habits, Face Your Fears and Change Your Life", author: "Bryan Collins", want_level: 10, status: "owned", done_to_read: False},
		{id: 125, book_title: "Atomic Habits", author: "James Clear", want_level: 9, status: "owned", done_to_read: False},
		{id: 126, book_title: "Midas Touch Why Some Entrepreneurs Get Rich-And Why Most Dont", author: "Donald J. Trump", want_level: 5, status: "owned", done_to_read: False},
		{id: 127, book_title: "How to talk to anyone: 92 little tricks for big success in relationships", author: "Leil Lowndes", want_level: 8, status: "owned", done_to_read: False},
		{id: 128, book_title: "Outliers: The Story of Success", author: "Malcolm Gladwell", want_level: 8, status: "owned", done_to_read: False},
		{id: 129, book_title: "Do the Work: Overcome Resistance and Get Out of Your Own Way", author: "Steven Pressfield", want_level: 8, status: "owned", done_to_read: False},
		{id: 130, book_title: "The Diary of Anne Frank", author: "Frank Anne", want_level: 10, status: "owned", done_to_read: False},
		{id: 131, book_title: "MONEY Master the Game - 7 Simple Steps to Financial Freedom", author: "Tony Robbins", want_level: 10, status: "owned", done_to_read: False},
		{id: 132, book_title: "Stock Investing For Dummies", author: "Paul Mladjenovic", want_level: 6, status: "owned", done_to_read: False},
		{id: 133, book_title: "The Art of Public Speaking The Original Tool for Improving Public Oration", author: "Dale Carnegie", want_level: 8, status: "owned", done_to_read: False},
		{id: 134, book_title: "Your Successful Real Estate Career", author: "Kenneth W. Edwards", want_level: 10, status: "owned", done_to_read: False},
		{id: 135, book_title: "Building Big Profits in Real Estate: A Guide for The New Investor", author: "Suzanne Caplan", want_level: 8, status: "owned", done_to_read: False},
		{id: 136, book_title: "Secure Your Financial Future Investing in Real Estate", author: "Martin Stone", want_level: 10, status: "owned", done_to_read: False},
		{id: 137, book_title: "Awaken the Giant Within How to Take Immediate Control of Your Mental, Emotional, Physical and Financial Destiny", author: "Tony Robbins", want_level: 9, status: "owned", done_to_read: False},
		{id: 138, book_title: "Civilization and Its Discontents", author: "Freud Sigmund", want_level: 7, status: "owned", done_to_read: False},
		{id: 139, book_title: "Compelling People The Hidden Qualities That Make Us Influential", author: "John Neffinger", want_level: 10, status: "owned", done_to_read: False},
		{id: 140, book_title: "Contagious Why Things Catch On", author: "Berger Jonah", want_level: 8, status: "owned", done_to_read: False},
		{id: 141, book_title: "Eat the Yolks Discover Paleo, fight food lies, and reclaim your health", author: "Wolfe", want_level: 8, status: "owned", done_to_read: False},
		{id: 142, book_title: "King of Capital The Remarkable Rise, Fall, and Rise Again of Steve Schwarzman and Blackstone", author: "David Carey", want_level: 6, status: "owned", done_to_read: False},
		{id: 143, book_title: "On the Heights of Despair", author: "E. M. Cioran", want_level: 10, status: "owned", done_to_read: False},
		{id: 144, book_title: "Red notice a true story of high finance, murder, and one mans fight for justice", author: "Bill Browder", want_level: 8, status: "owned", done_to_read: False},
		{id: 145, book_title: "The End of Faith Religion, Terror, and the Future of Reason", author: "Sam Harris", want_level: 9, status: "owned", done_to_read: False},
		{id: 146, book_title: "The Moral Landscape How Science Can Determine Human Values", author: "Sam Harris", want_level: 9, status: "owned", done_to_read: False},
		{id: 147, book_title: "The trouble with being born", author: "E. M. Cioran", want_level: 10, status: "owned", done_to_read: False},
		{id: 148, book_title: "The Social Media Marketing Book", author: "Dan Zarrella", want_level: 9, status: "owned", done_to_read: False},
		{id: 149, book_title: "Sell with a Story How to Capture Attention, Build Trust, and Close the Sale", author: "Paul Smith", want_level: 8, status: "owned", done_to_read: False},
		{id: 150, book_title: "Smart Pricing How Google, Priceline, and Leading Businesses Use Pricing Innovation for Profitability", author: "Jagmohan Raju", want_level: 8, status: "owned", done_to_read: False},
		{id: 151, book_title: "Assassins Creed The Secret Crusade", author: "Bowden Oliver", want_level: 6, status: "owned", done_to_read: False},
		{id: 152, book_title: "Assassins Creed Revelations", author: "Oliver Bowden", want_level: 5, status: "owned", done_to_read: False},
		{id: 153, book_title: "Guns, Germs, and Steel The Fates of Human Societies", author: "Jared M. Diamond", want_level: 10, status: "owned", done_to_read: False},
		{id: 154, book_title: "Long Walk to Freedom The Autobiography of Nelson Mandela", author: "Nelson Mandela", want_level: 10, status: "owned", done_to_read: False},
		{id: 155, book_title: "The Audacity of Hope. Thoughts on Reclaiming the American Dream", author: "Barack Obama", want_level: 9, status: "owned", done_to_read: False},
		{id: 156, book_title: "The Sales Bible The Ultimate Sales Resource, Revised Edition", author: "Jeffrey Gitomer", want_level: 9, status: "owned", done_to_read: False},
		{id: 157, book_title: "Building Structures Illustrated Patterns, Systems, and Design", author: "Francis D. K. Ching", want_level: 10, status: "owned", done_to_read: False},
		{id: 158, book_title: "R for Data Science Import, Tidy, Transform, Visualize, and Model Data", author: "Hadley Wickham", want_level: 9, status: "owned", done_to_read: False},
		{id: 159, book_title: "Regular Expression Pocket Reference Regular Expressions for Perl, Ruby, PHP, Python, C, Java and .NET", author: "Tony Stubblebine", want_level: 10, status: "owned", done_to_read: False},
		{id: 160, book_title: "Learn Rails 5.2 Accelerated Web Development with Ruby on Rails", author: "Wintermeyer", want_level: 8, status: "owned", done_to_read: False},
		{id: 161, book_title: "Building Microservices", author: "Sam Newman", want_level: 10, status: "owned", done_to_read: False},
		{id: 162, book_title: "Superintelligence Paths, Dangers, Strategies", author: "Nick Bostrom", want_level: 10, status: "owned", done_to_read: False},
		{id: 163, book_title: "Blake Masters Zero to One Notes on Startups, or How to Build the Future Crown Business", author: "Peter Thiel", want_level: 8, status: "owned", done_to_read: False},
		{id: 164, book_title: "Unlimited Memory How to Use Advanced Learning Strategies to Learn Faster, Remember More and be More Productive", author: "Kevin Horsley", want_level: 7, status: "owned", done_to_read: False},
		{id: 165, book_title: "How to Sleep Well", author: "Neil Stanley", want_level: 10, status: "owned", done_to_read: False},
		{id: 166, book_title: "The god delusion", author: "Richard Dawkins", want_level: 10, status: "owned", done_to_read: False},
		{id: 167, book_title: "How to Change Your Mind What the New Science of Psychedelics Teaches Us About Consciousness, Dying, Addiction, Depression, and Transcendence", author: "Michael Pollan", want_level: 10, status: "owned", done_to_read: False},
		{id: 168, book_title: "Notes from Underground", author: "Fyodor Dostoyevsky", want_level: 10, status: "owned", done_to_read: False},
		{id: 169, book_title: "It Doesn’t Have to Be Crazy at Work", author: "Jason Fried", want_level: 10, status: "owned", done_to_read: False},
		{id: 170, book_title: "Fiasco The Inside Story of a Wall Street Trader", author: "Frank Partnoy", want_level: 10, status: "owned", done_to_read: False},
		{id: 171, book_title: "The Warren Buffett Way", author: "Robert G. Hagstrom", want_level: 10, status: "owned", done_to_read: False},
		{id: 172, book_title: "The Emotionally Intelligent Manager How to Develop and Use the Four Key Emotional Skills of Leadership", author: "David R. Caruso", want_level: 10, status: "owned", done_to_read: False},
		{id: 173, book_title: "Negotiating For Dummies", author: "Michael C. Donaldson", want_level: 10, status: "owned", done_to_read: False},
		{id: 174, book_title: "Presidents of War", author: "Michael Beschloss", want_level: 10, status: "owned", done_to_read: False},
		{id: 175, book_title: "Mastering the Market Cycle: Getting the Odds on Your Side", author: "Howard Marks", want_level: 10, status: "owned", done_to_read: False},
		{id: 176, book_title: "The Examined Life: How We Lose and Find Ourselves", author: "Stephen Grosz", want_level: 10, status: "not owned", done_to_read: False},
		{id: 177, book_title: "Deep learning adaptive computation and machine learning", author: "Bengio", want_level: 10, status: "owned", done_to_read: False},
		{id: 178, book_title: "Machine Learning with Python Cookbook Practical Solutions from Preprocessing to Deep Learning", author: "Chris Albon", want_level: 9, status: "owned", done_to_read: False},
		{id: 179, book_title: "Games People Play The Psychology of Human Relationships", author: "Eric Berne", want_level: 8, status: "owned", done_to_read: False},
		{id: 180, book_title: "Dreamland The True Tale of Americas Opiate Epidemic", author: "Sam Quinones", want_level: 7, status: "owned", done_to_read: False},
		{id: 181, book_title: "Game theory through examples", author: "Prisner", want_level: 5, status: "owned", done_to_read: False},
		{id: 183, book_title: "Playing for Real A Text on Game Theory", author: "Ken Binmore", want_level: 6, status: "owned", done_to_read: False},
		{id: 184, book_title: "Your Creative Mind How to Disrupt Your Thinking, Abandon Your Comfort Zone, and Develop Bold New Strategies", author: "Scott Cochrane", want_level: 10, status: "owned", done_to_read: False},
		{id: 185, book_title: "The Gift of Fear", author: "Gavin de Becker", want_level: 9, status: "owned", done_to_read: False},
		{id: 186, book_title: "Deep Learning A Practitioners Approach", author: "J. Patterson, A. Gibson", want_level: 9, status: "owned", done_to_read: False},
		{id: 187, book_title: "Built to last", author: "Jim Collins", want_level: 10, status: "not owned", done_to_read: False},
		{id: 188, book_title: "Memos from the Chairman", author: "Alan C. Greenberg", want_level: 10, status: "owned", done_to_read: False},
		{id: 189, book_title: "Data-Driven Marketing: The 15 Metrics Everyone in Marketing Should Know", author: "Mark Jeffrey", want_level: 10, status: "owned", done_to_read: False},
		{id: 190, book_title: "Software Development From A to Z: A Deep Dive into all the Roles Involved in the Creation of Software", author: "Olga Filipova", want_level: 10, status: "owned", done_to_read: False},
		{id: 191, book_title: "The algorithm design manual", author: "Steven Skiena", want_level: 5, status: "owned", done_to_read: False},
		{id: 192, book_title: "Think: Why You Should Question Everything", author: "Guy P. Harrison", want_level: 10, status: "owned", done_to_read: False},
		{id: 193, book_title: "Maximum Influence: The 12 Universal Laws of Power", author: "Kurt W. Mortensen", want_level: 8, status: "owned", done_to_read: False},
		{id: 194, book_title: "No Excuses!: The Power of Self-Discipline", author: "Brian Tracy", want_level: 9, status: "owned", done_to_read: False},
		{id: 195, book_title: "Breathe: The Simple, Revolutionary 14 Day Program to Improve Your Mental and Physical Health", author: "Belisa Vranich", want_level: 9, status: "owned", done_to_read: False},
		{id: 196, book_title: "The Culture Code: The Secrets of Highly Successful Groups", author: "Daniel Coyle", want_level: 8, status: "owned", done_to_read: False},
		{id: 197, book_title: "We Have a Deal: How to Negotiate with Intelligence, Flexibility and Power", author: "Natalie Reynolds", want_level: 7, status: "owned", done_to_read: False},
		{id: 198, book_title: "Get Momentum How to Start When You’re Stuck", author: "Jason W. Womack", want_level: 10, done_to_read: False},
		{id: 199, book_title: "Programming Rust Fast, Safe Systems Development", author: "Jim Blandy", want_level: 9, done_to_read: False},
		{id: 200, book_title: "The Go Programming Language", author: "Alan A. A", want_level: 9, done_to_read: False},
		{id: 201, book_title: "Training Your Brain For Dummies", author: "Tracy Packiam Alloway", want_level: 10, done_to_read: False},
		{id: 202, book_title: "Trump Strategies for Real Estate Billionaire Lessons for the Small Investor", author: "George Ross", want_level: 6, done_to_read: False},
		{id: 203, book_title: "Becoming a Better Programmer A Handbook for People Who Care About Code", author: "Pete Goodliffe", want_level: 9, done_to_read: False},
		{id: 204, book_title: "Technology Strategy Patterns Architecture as Strategy", author: "Eben Hewitt", want_level: 10, done_to_read: False},
		{id: 205, book_title: "Test-Driven Development with Python Obey the Testing Goat Using Django, Selenium, and JavaScript", author: "Harry J. W. Percival", want_level: 10, done_to_read: False},
		{id: 206, book_title: "Flask Web Development Developing Web Applications with Python", author: "Miguel Grinberg", want_level: 8, done_to_read: False},
		{id: 207, book_title: "Coding Theory Algorithms, Architectures, and Applications", author: "Andre Neubauer", want_level: 8, done_to_read: False},
		{id: 208, book_title: "The Performance of Open Source Applications", author: "Tavish Armstrong", want_level: 10, done_to_read: False},
		{id: 209, book_title: "The Architecture Of Open Source Applications, Volume II", author: "Amy Brown", want_level: 10, done_to_read: False},
		{id: 210, book_title: "The Power of Habit Why We Do What We Do in Life and Business", author: "Charles Duhigg", want_level: 10, done_to_read: False},
		{id: 211, book_title: "The Architecture Of Open Source Applications", author: "Amy Brown", want_level: 10, done_to_read: False},
		{id: 212, book_title: "Investing in International Real Estate for Dummies", author: "TaTk Dummies", want_level: 10, done_to_read: False},
		{id: 213, book_title: "The Millionaire Real Estate Agent Its Not About the Money...Its About Being the Best You Can Be", author: "Gary Keller", want_level: 9, done_to_read: False},
		{id: 214, book_title: "Head First Object-Oriented Analysis and Design", author: "Brett D. McLaughlin", want_level: 9, done_to_read: False},
		{id: 215, book_title: "The Heart of the Deal How to Invest and Negotiate like a Real Estate Mogul", author: "Anthony Lolli", want_level: 8, done_to_read: False},
		{id: 216, book_title: "The Upstarts How Uber, Airbnb, and the Killer Companies of the New Silicon Valley Are Changing the World", author: "Brad Stone", want_level: 10, done_to_read: False},
		{id: 217, book_title: "Bring Your Whole Self to Work How Vulnerability Unlocks Creativity, Connection, and Performance", author: "Mike Robbins", want_level: 8, done_to_read: False},
		{id: 218, book_title: "Head First Software Development", author: "Dan Pilone", want_level: 9, done_to_read: False},
		{id: 219, book_title: "Designing Web APIs Building APIs That Developers Love", author: "Brenda Jin Saurabh Sahni Amir Shevat", want_level: 9, done_to_read: False},
		{id: 220, book_title: "Designing Data-Intensive Applications The Big Ideas Behind Reliable, Scalable, and Maintainable Systems", author: " Martin Kleppmann", want_level: 10, done_to_read: False},
		{id: 221, book_title: "Using Docker Developing and Deploying Software with Containers", author: "Adrian Mouat", want_level: 8, done_to_read: False},
		{id: 222, book_title: "Deep Learning with Python", author: "Francois Chollet", want_level: 10, done_to_read: False},
		{id: 223, book_title: "Deep Learning from Scratch Building with Python from First Principles", author: "Seth Weidman", want_level: 9, done_to_read: False},
		{id: 224, book_title: "Hands-On Unsupervised Learning Using Python How to Build Applied Machine Learning Solutions from Unlabeled Data", author: "Ankur A Patel", want_level: 9, done_to_read: False},
		{id: 225, book_title: "Lean UX Designing Great Products with Agile Teams", author: "Jeff Gothelf", want_level: 10, done_to_read: False},
		{id: 226, book_title: "Data Science from Scratch First Principles with Python", author: "Joel Grus", want_level: 9, done_to_read: False},
		{id: 227, book_title: "Data Analytics Practical Guide to Leveraging the Power of Algorithms, Data Science, Data Mining, Statistics, Big Data, and Predictive Analysis to Improve Business, Work, and Life", author: "Arthur Zhang ", want_level: 9, done_to_read: False},
		{id: 228, book_title: "Business Analysis Methodology Book Business Analysts Guide to Requirements Analysis, Lean UX Design and Project Management at Lean Enterprises and Lean Startups", author: "Yayici", want_level: 10, done_to_read: False},
		{id: 229, book_title: "The Non-Designers Design Book", author: "Robin Williams", want_level: 10, done_to_read: False},
		{id: 230, book_title: "UX Fundamentals for Non-UX Professionals User Experience Principles for Managers, Writers, Designers, and Developers", author: "Edward Stull", want_level: 10, done_to_read: False},
		{id: 231, book_title: "The Design of Everyday Things - Revised and Expanded Edition", author: "Don Norman", want_level: 8, done_to_read: False},
		{id: 232, book_title: "Implementation Patterns", author: "Kent Beck", want_level: 10, done_to_read: False},
		{id: 233, book_title: "501 Web site secrets unleash the power of Google, Amazon, eBay, and more", author: "Michael Miller", want_level: 8, done_to_read: False},
		{id: 234, book_title: "Passive income  develop a passive income empire  complete beginners guide to building riches through multiple streams", author: "Wolf, Simon", want_level: 10, done_to_read: False},
		{id: 235, book_title: "Passive Income 30 Strategies and Ideas To Start an Online Business and Acquiring Financial Freedom", author: "Richard Gadson", want_level: 9, done_to_read: False},
		{id: 236, book_title: "Smarter Faster Better The Secrets of Being Productive in Life and Business", author: "Charles Duhigg", want_level: 10, done_to_read: False},
		{id: 237, book_title: "Steve Jobs", author: "Isaacson Walter", want_level: 7, done_to_read: False},
		{id: 238, book_title: "The Leadership Training Activity Book 50 Exercises for Building Effective Leaders", author: "Lois B. Hart", want_level: 9, done_to_read: False},
		{id: 239, book_title: "The Real Book of Real Estate Real Experts. Real Stories. Real Life.", author: "Robert T. Kiyosaki", want_level: 9, done_to_read: False},
		{id: 240, book_title: "A Passion for Mathematics - Numbers, Puzzles, Madness, Religion, and the Quest for Reality", author: "Clifford A. Pickover", want_level: 6, done_to_read: False},
		{id: 241, book_title: "Getting Started with TypeScript  Includes Introduction to Angular", author: "Thomas Claudius Huber", want_level: 10, done_to_read: False},
		{id: 242, book_title: "Logic made easy how to know when language deceives you", author: "Deborah J. Bennett", want_level: 10, done_to_read: False},
		{id: 243, book_title: "The temptation to exist", author: "Emil Cioran", want_level: 10, done_to_read: False},
		{id: 244, book_title: "The Psychology Book", author: "DK", want_level: 8, done_to_read: False},
		{id: 245, book_title: "The classical music book", author: "DK", want_level: 9, done_to_read: False},
		# {id: 244, book_title: , author: , want_level, done_to_read: },
	]
