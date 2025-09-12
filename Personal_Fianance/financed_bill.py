from bill import *


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

    def process_day(self, date_in):
        day = date_in.day
        if day == self.get_payment_day():
            self.make_payment(date_in=date_in)
