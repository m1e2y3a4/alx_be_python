# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: called when the object is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """
        Informal string representation.
        Example: "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Official string representation that could be used to recreate the object.
        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
