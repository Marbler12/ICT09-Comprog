#Library Management System

class Book:
		def __init__(self,title,author,year,isbn,pages):
			self.title = title
			self.author = author
			self.year = year
			self.isbn = isbn
			self.pages = pages
			
		def book_details(self):			
			return (
            f"{self.title} by {self.author}\n"
            f"Year of Publication: {self.year}\n"
            f"ISBN: {self.isbn}\n"
            f"No. of Pages: {self.pages}\n"
        )

			
class Library:
	def __init__(self):
		self.booklist = []
		
	def add_book(self,book):			 
		 self.booklist.append(book)
			
	def display(self):
		if not self.booklist:
			print("No available books in the library.")
		else:
			print("Available Books in the Library:")
			for book in self.booklist:
				print(f"- {book.title}")
	
	def search_book(self,title):
		results = [book for book in self.booklist if title.lower() in book.title.lower()]
		return results
		
library = Library()

while True:
	print("\nLibrary Menu:")
	print("1.Add Book")
	print("2.Display Books")
	print("3.Search Book by title")
	print("4.Exit")
	print()
	choice = input("Enter choice:")
	print()
	
#Add Books	
	if choice == "1":		
		title = input("Enter book title: ")
		author = input("Enter author: ")
		while True:
		    year_input = input("Enter year of publication: ")
		    try:
		        year = int(year_input)
		        break  
		    except ValueError:
		        print("Invalid input, try again.")
		        print()
		isbn = input("Enter book ISBN: ")	
			
		while True:
		    pages_input = input("Enter no. of pages: ")
		    try:
		        pages = int(pages_input)
		        break  
		    except ValueError:
		        print("Invalid input, try again.")    
		        print()    
						
		new_book = Book(title,author,year,isbn,pages)
		library.add_book(new_book)
		print("New book added to library.")

#Display all books available
	elif choice == "2":
		library.display()

#Search book by title	
	elif choice == "3":
		search_title = input("Enter book title:")
		search_results = library.search_book(search_title)
		if search_results:
			print("Search Results:")
			for book in search_results:
				print(book.book_details())
		else:
			print("Book not found.")

#Exit Program	
	elif choice == "4":
		print("Exiting Library Managing System.")
		break
	
	else:
		print("Invalid choice. Try again.")


	
		
		
	
	
				
	

