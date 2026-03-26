class Book:
    """
    Represents a book in the library.

    Design Decisions:
    - Encapsulated attributes
    - Tracks availability internally
    - Simple, primitive operations
    """

    def __init__(self, title, author, isbn, year):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._year = year
        self._is_borrowed = False

    # -------------------------
    # Properties
    # -------------------------
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    # -------------------------
    # Operations
    # -------------------------
    def borrow(self):
        """Marks book as borrowed if available."""
        if self._is_borrowed:
            return False
        self._is_borrowed = True
        return True

    def return_book(self):
        """Marks book as returned."""
        self._is_borrowed = False

    def is_available(self):
        """Checks if book is available."""
        return not self._is_borrowed