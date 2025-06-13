#This example simulates a simple library management system.
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.is_available}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def borrow_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            if book.is_available:
                book.is_available = False
                print(f"Book '{book.title}' borrowed successfully.")
            else:
                print(f"Book '{book.title}' is currently unavailable.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            if not book.is_available:
                book.is_available = True
                print(f"Book '{book.title}' returned successfully.")
            else:
                print(f"Book '{book.title}' is already available.")
        else:
            print("Book not found.")

# Main program
library = Library()

# Adding books
library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien", "101"))
library.add_book(Book("Pride and Prejudice", "Jane Austen", "102"))
library.add_book(Book("1984", "George Orwell", "103"))

while True:
    print("\nLibrary Management System")
    print("1. Display all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        book_id = input("Enter the book ID to borrow: ")
        library.borrow_book(book_id)
    elif choice == '3':
        book_id = input("Enter the book ID to return: ")
        library.return_book(book_id)
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")