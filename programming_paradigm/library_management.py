#!/usr/bin/python3
"""
library_management.py

Defines Book and Library classes for a simple
library management system.
"""


class Book:
    """
    Represents a single book in the library.

    Public attributes:
        title (str)
        author (str)

    Private attributes:
        _is_checked_out (bool): True if the book is checked out.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """
    Represents a library that manages a collection of books.

    Private attributes:
        _books (list[Book]): list of Book instances.
    """

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """
        Add a Book instance to the library.
        """
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """
        Check out the first available book with the given title.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                break

    def return_book(self, title):
        """
        Return the first checked-out book with the given title.
        """
        for book in self._books:
            if book.title == title and not book.is_available() is False:
                # simpler: if book.title == title and book._is_checked_out:
                book.return_book()
                break

    def list_available_books(self):
        """
        Print all available books in the format:
        'Title by Author'
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
