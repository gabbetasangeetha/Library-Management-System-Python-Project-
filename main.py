import re
from lib import Member, Book, Library

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_lent = False

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Lent out: {self.is_lent}"

class Library:
    def __init__(self):
        self.books = []
        self._load_initial_books()

    def _load_initial_books(self):
        self.add_book('1', '1984', 'George Orwell')
        self.add_book('2', 'To Kill a Mockingbird', 'Harper Lee')
        self.add_book('3', 'The Great Gatsby', 'F. Scott Fitzgerald')
        self.add_book('4', 'Moby Dick', 'Herman Melville')
        self.add_book('5', 'War and Peace', 'Leo Tolstoy')

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Available books in the library:")
        for book in self.books:
            print(book)

    def lend_book(self, book_id):
        book = next((b for b in self.books if b.book_id == book_id and not b.is_lent), None)
        if book:
            book.is_lent = True
            print(f"Book '{book.title}' lent out.")
        else:
            print("Lending operation failed. Book might be already lent or does not exist.")

    def return_book(self, book_id):
        book = next((b for b in self.books if b.book_id == book_id and b.is_lent), None)
        if book:
            book.is_lent = False
            print(f"Book '{book.title}' returned.")
        else:
            print("Return operation failed. Book might not be lent out or does not exist.")

    def search_book(self, title):
        book = next((b for b in self.books if b.title.lower() == title.lower()), None)
        if book:
            print(f"Book found: {book}")
        else:
            print(f"No book found with title '{title}'.")

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com'
    return re.match(pattern, email)

def validate_password(password):

    return len(password) >= 4

def login():
    print("Login to Library Management System")

    while True:
        print("Welcome")
        email = input("Enter email: ")
        if not validate_email(email):
            print("Invalid email format. Please enter a valid email address.")
            continue

        password = input("Enter password (at least 4 characters): ")
        if not validate_password(password):
            print("Password should be at least 4 characters long.")
            continue

        print("Login successful!")
        return True

def main():
    if not login():
        return
    
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(book_id, title, author)
            print(f"Book '{title}' added to the library.")

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            book_id = input("Enter book ID to lend: ")
            library.lend_book(book_id)

        elif choice == '4':
            book_id = input("Enter book ID to return: ")
            library.return_book(book_id)

        elif choice == '5':
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == '6':
            print("Thank you, visit again")
            break

if __name__ == '__main__':
    main()