from bill import *


class RecurringBill(Bill):
    def __init__(self, name_in, balance_in, initial_payment_date_in, monthly_payment_in, payment_method_in,
                 recurring_type_in, round_up_in=False):
        super().__init__(name_in=name_in, balance_in=balance_in, payment_day_in=initial_payment_date_in.day,
                         monthly_payment_in=monthly_payment_in, payment_method_in=payment_method_in,
                         billing_type='Recurring Bill',
                         round_up=round_up_in)
        self.__total_paid = 0
        self.__initial_payment_date = initial_payment_date_in
        self.__recurring_type = recurring_type_in

    # Method to apply the payment to the balance
    def make_payment(self, date_in):
        # Add the monthly payment to the total payments made.
        self.__total_paid += self.get_monthly_payment()
        self.payment_method.make_a_transaction(date_in=date_in, action=f'{self.get_bill_name()}-Payment', credit=0,
                                               debit=self.get_monthly_payment())

    def get_total_paid(self):
        # immutable type double
        return self.__total_paid

    def process_day(self, date_in):
        if self.trigger_day(date_in):
            # Make Account Contribution
            self.make_payment(date_in=date_in)

    def trigger_day(self, date_in):
        # We make a payment 1 time a month
        if self.__recurring_type == 3 and min(self.__initial_payment_date.day, 28) == date_in.day:
            return True
        # Bi weekly payment
        elif self.__recurring_type == 2 and abs(self.__initial_payment_date - date_in).days % 14 == 0:
            return True
        # Weekly payments
        elif self.__recurring_type == 1 and abs(self.__initial_payment_date - date_in).days % 7 == 0:
            return True
        return False
