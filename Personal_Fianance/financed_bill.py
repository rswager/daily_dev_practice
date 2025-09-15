from bill import *

def is_leap(year_in):
    if (year_in % 4) == 0:
        if (year_in % 100) == 0 and year_in % 400 != 0:
            return False
        return True
    return False

class FinancedBill(Bill):
    def __init__(self, name_in, balance_in, payment_day_in, monthly_payment_in, payment_method_in, round_up_in=False):
        super().__init__(name_in=name_in, balance_in=balance_in, payment_day_in=payment_day_in,
                         monthly_payment_in=monthly_payment_in, payment_method_in=payment_method_in,
                         billing_type='Financed Bill', round_up=round_up_in)

    # Method to apply the payment to the balance
    def make_payment(self, date_in):
        if self.get_balance()!= 0:
            # If balance is more than payment we subtract it and return 0
            if self.get_balance() >= self.get_monthly_payment():
                self.set_balance(self.get_balance() - self.get_monthly_payment())
                # Apply payment to payment method
                self.payment_method.make_a_transaction(date_in=date_in, action=f'{self.get_bill_name()}-Payment',
                                                       credit=0, debit=self.get_monthly_payment())
            # If balance is less than payment we zero out the balance and return the difference ( to credit it back)
            else:
                # Apply payment to payment method
                self.payment_method.make_a_transaction(date_in=date_in, action=f'{self.get_bill_name()}-Payment',
                                                       credit=0, debit=self.get_balance())
                self.set_balance(0)

    def calculate_interest(self, date_in):
        if abs(self.get_balance()) > 0:
            n_days = 365 if not is_leap(date_in.year) else 366
            interest = round((abs(self.get_balance())*(self.__apr_rate / n_days)), 2)
            self.__interest_paid_to_date += interest
            self.make_a_transaction(date_in=date_in, action='Daily Interest',
                                    credit=0, debit=interest)

    def process_day(self, date_in):
        day = date_in.day
        # Calculate Interest Daily
        self.calculate_interest(date_in=date_in)

        # Check to see if we need to make a payment
        if day == self.get_payment_day():
            self.make_payment(date_in=date_in)

    def make_a_transaction(self, date_in, action, credit, debit):
        self.set_balance(self.get_balance() + credit - debit)
        self.__add_to_ledger(date_in=date_in, action=action, credit=credit, debit=debit)

    def get_interest_paid_to_date(self):
        # immutable type double
        return self.__interest_paid_to_date
