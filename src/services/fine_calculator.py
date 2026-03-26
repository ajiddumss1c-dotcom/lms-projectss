class FineCalculator:
    """
    Calculates fines using configurable rules.

    Design:
    - Isolates changeable business logic
    """

    def calculate_fine(self, days_overdue):
        if days_overdue <= 0:
            return 0.0
        elif days_overdue <= 7:
            return days_overdue * 0.50
        else:
            return (7 * 0.50) + (days_overdue - 7) * 1.00