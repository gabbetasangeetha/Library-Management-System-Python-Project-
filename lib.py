class Member: 
    def _init_(self, member_id, name):
        super()._init_(member_id, name)
        self.borrowed_books = []

    def get_details(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"ID: {self.user_id}, Name: {self.name}, Borrowed Books: {borrowed_titles}"

    def _str_(self):
        return self.get_details()

class Book:
    def _init_(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_lent = False
    
    def _str_(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Lent: {self.is_lent}"

class Library:
    def _init_(self):
        self.books = []
        self.members = []
        self.lending_stack = []
        self._load_initial_books()