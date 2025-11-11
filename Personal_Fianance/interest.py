from calendar import isleap
from datetime import date

class Interest:
    def __init__(self, apr_rate_in: float):
        if not (0 <= apr_rate_in <= 1):
            raise ValueError("APR must be a percentage as a fraction between 0 and 1 (e.g., 5% → 0.05)")
        self._apr_rate: float = apr_rate_in
        self._interest_to_date: float = 0

    def calculate_daily_interest(self, balance_in: float, date_in: date) -> float:
        """Calculate daily interest and log it in the ledger."""
        interest = 0
        if abs(balance_in) > 0:
            n_days = 365 if not isleap(date_in.year) else 366
            interest = round(abs(balance_in) * (self._apr_rate / n_days), 2)

            # Update cumulative interest
            self._interest_to_date += interest

        return interest

    @property
    def interest_to_date(self):
        return self._interest_to_date