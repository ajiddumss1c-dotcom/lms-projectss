class BookCollection:
    """
    ADT for managing books.

    - Uses dictionary internally (hidden)
    - Key = ISBN
    """

    def __init__(self):
        self._books = {}

    def add_book(self, book):
        if book.isbn in self._books:
            raise ValueError("Book already exists")

        self._books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn not in self._books:
            raise KeyError("Book not found")

        del self._books[isbn]

    def find_by_isbn(self, isbn):
        return self._books.get(isbn)

    def find_by_title(self, title):
        return [
            book for book in self._books.values()
            if title.lower() in book.title.lower()
        ]

    def get_all_books(self):
        return list(self._books.values())

    def count(self):
        return len(self._books)