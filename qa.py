# Design a Library class that manages books and their availability. The system should include the following:

# Classes:

# Book:

# Attributes:
# title (string): Title of the book.
# author (string): Author of the book.
# copies_available (int): Number of copies available.
# Methods:
# add_copies(number): Adds copies to the book.
# borrow_book(): Decreases available copies if there are copies; otherwise, print "Not available."
# return_book(): Increases available copies.
# Library:

# Attributes:
# books (list): A list of Book objects.
# Methods:
# add_book(book): Adds a new Book object to the library.
# search_book(title): Searches for a book by title and returns it.
# borrow_book(title): Allows a user to borrow a book if it's available.
# return_book(title): Allows a user to return a borrowed book.
# list_books(): Lists all books in the library with their availability.
# Tasks:

# Add three books to the library:
# "1984" by George Orwell (5 copies)
# "To Kill a Mockingbird" by Harper Lee (3 copies)
# "The Great Gatsby" by F. Scott Fitzgerald (4 copies)
# Borrow "1984" and "The Great Gatsby."
# Return "1984."
# Print all books in the library with their current availability.


class Book:
    def __init__(self,title,author,copies_a):
        self.title=title
        self.author=author
        self.copies_a=copies_a
    def add_copies(self,number):
        self.copies_a=self.copies_a+number
    def borrow_book(self):
        if self.copies_a >0:
            self.copies_a=self.copies_a-1
        else:
            print("not available")
    def return_book(self):
        self.copies_a=self.copies_a+1

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def search_book(self,title):
        for book in self.books:
            if book.title==title:
               return book
        return None
    def list_book(self):
        if self.books:
            for book in self.books:
                print(book.title,book.author,book.copies_a)
        else:
            print("no books ")
obj1=Library()
book1 = Book("1984", "George Orwell", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 3)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 4)
obj1.add_book(book1)
obj1.add_book(book2)
obj1.add_book(book3)
obj1.list_book()
        
                
        
            
        
        
        
        
        
            
        
        
        
    