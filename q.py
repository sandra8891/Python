class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def add_copies(self, number):
        """Adds the specified number of copies to the book."""
        self.copies_available += number

    def borrow_book(self):
        """Decreases the available copies of the book if available, otherwise prints 'Not available'."""
        if self.copies_available > 0:
            self.copies_available -= 1
        else:
            print(f"'{self.title}' is not available.")

    def return_book(self):
        """Increases the available copies of the book."""
        self.copies_available += 1


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a new Book object to the library."""
        self.books.append(book)

    def search_book(self, title):
        """Searches for a book by title and returns the book if found, otherwise None."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        """Allows a user to borrow a book if available."""
        book = self.search_book(title)
        if book:
            book.borrow_book()
        else:
            print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Allows a user to return a borrowed book."""
        book = self.search_book(title)
        if book:
            book.return_book()
        else:
            print(f"'{title}' not found in the library.")

    def list_books(self):
        """Lists all books in the library with their current availability."""
        if self.books:
            print("Library Inventory:")
            for book in self.books:
                print(f"'{book.title}' by {book.author} - {book.copies_available} copies available.")
        else:
            print("No books in the library.")


# Creating Library object
library = Library()

# # Adding books to the library
book1 = Book("1984", "George Orwell", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 3)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 4)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Borrowing books
library.borrow_book("1984")
library.borrow_book("The Great Gatsby")

# Returning a book
# library.return_book("1984")
library.search_book("1984")

# Printing the list of all books in the library with their availability
library.list_books()


