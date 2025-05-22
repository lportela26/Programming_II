class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', available={self.available})"

class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)

    def borrow(self, title1):
        for book in self.catalog:
            if book.title == title1 and book.available:
                book.available = False
                return f"You borrowed: {book}"
        return "Book not available."

    def return_book(self, title):
        for book in self.catalog:
            if book.title == title and not book.available:
                book.available = True
                return f"You returned: {book}"
        return "This book wasn't borrowed."

    def list_available(self):
        return [book for book in self.catalog if book.available]



b1 = Book("1984", "George Orwell")
b2 = Book("Sapiens", "Yuval Noah Harari")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

print(lib.borrow("1984"))
print(lib.borrow("1984"))
print(lib.return_book("1984"))
print(lib.list_available())