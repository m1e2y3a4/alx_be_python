# library_system.py

class Book:
    def __init__(self, title, author):
        """Base Book class with common attributes."""
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        EBook class that inherits from Book and adds file_size.
        file_size is expected to be an integer (e.g., in KB).
        """
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        PrintBook class that inherits from Book and adds page_count.
        page_count is expected to be an integer.
        """
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        """Library uses composition to manage a collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book stored in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}"
                )
            else:
                # Plain Book instance
                print(f"Book: {book.title} by {book.author}")
