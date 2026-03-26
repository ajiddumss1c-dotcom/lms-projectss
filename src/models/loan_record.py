from datetime import date

class LoanRecord:
    """
    Represents a borrowing transaction.

    Design Decisions:
    - Links Member and Book
    - Encapsulates loan lifecycle
    """

    def __init__(self, book, member, checkout_date, due_date):
        self._book = book
        self._member = member
        self._checkout_date = checkout_date
        self._due_date = due_date
        self._return_date = None

    def mark_returned(self, return_date):
        """Marks book as returned."""
        self._return_date = return_date

    def is_overdue(self, current_date):
        """Checks if loan is overdue."""
        return (
            self._return_date is None and
            current_date > self._due_date
        )

    def get_due_date(self):
        return self._due_date