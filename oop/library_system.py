# library_system.py

class Book:
    def __init__(self, title, author):
        # Base Book class with common attributes
        self.title = title
        self.author = author

    def __str__(self):
        # String representation for a regular book
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        # EBook inherits from Book and adds file_size
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        # String representation for an ebook
        return (
            f"EBook: {self.title} by {self.author}, "
            f"File Size: {self.file_size}KB"
        )


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # PrintBook inherits from Book and adds page_count
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # String representation for a printed book
        return (
            f"PrintBook: {self.title} by {self.author}, "
            f"Page Count: {self.page_count}"
        )


class Library:
    def __init__(self):
        # Library uses composition to hold a list of books
        self.books = []

    def add_book(self, book):
        # Add a Book, EBook, or PrintBook instance
        self.books.append(book)

    def list_books(self):
        # Print details of each book (polymorphic via __str__)
        for book in self.books:
            print(book)
