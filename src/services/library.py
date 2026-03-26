from datetime import timedelta

class Library:
    """
    Main system controller.

    Responsibilities:
    - Coordinates books, members, and loans
    """

    LOAN_PERIOD_DAYS = 14

    def __init__(self):
        self._books = BookCollection()
        self._members = MemberCollection()
        self._loans = []
        self._fine_calculator = FineCalculator()

    # -------------------------
    # Book Operations
    # -------------------------
    def add_book(self, book):
        self._books.add_book(book)

    def find_book(self, isbn):
        return self._books.find_by_isbn(isbn)

    # -------------------------
    # Member Operations
    # -------------------------
    def register_member(self, member):
        self._members.add_member(member)

    def find_member(self, member_id):
        return self._members.find_by_id(member_id)

    # -------------------------
    # Loan Operations
    # -------------------------
    def check_out_book(self, member_id, isbn, checkout_date):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return False, "Invalid member or book"

        if not book.is_available():
            return False, "Book not available"

        if not member.borrow_book(book):
            return False, "Borrow limit reached"

        due_date = checkout_date + timedelta(days=self.LOAN_PERIOD_DAYS)

        loan = LoanRecord(book, member, checkout_date, due_date)
        self._loans.append(loan)

        book.borrow()

        return True, "Book checked out"

    def return_book(self, member_id, isbn, return_date):
        for loan in self._loans:
            if (loan._member.member_id == member_id and
                loan._book.isbn == isbn and
                loan._return_date is None):

                loan.mark_returned(return_date)
                loan._book.return_book()
                loan._member.return_book(loan._book)

                return True, "Book returned"

        return False, "Loan not found"

    # -------------------------
    # Fine Calculation
    # -------------------------
    def calculate_member_fines(self, member_id, current_date):
        total = 0.0

        for loan in self._loans:
            if loan._member.member_id == member_id:
                if loan.is_overdue(current_date):
                    days = (current_date - loan.get_due_date()).days
                    total += self._fine_calculator.calculate_fine(days)

        return total