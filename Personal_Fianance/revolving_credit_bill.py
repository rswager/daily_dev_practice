from bill import *
from bank_account import *
from income import Income


def is_leap(year_in):
    if (year_in % 4) == 0:
        if (year_in % 100) == 0 and year_in % 400 != 0:
            return False
        return True
    return False


class RevolvingCreditBill(Bill):
    def __init__(self, name_in, balance_in, payment_day_in, monthly_payment_in, apr_rate_in, credit_limit_in,
                 payment_method_in, round_up_in=False):
        super().__init__(name_in=name_in, balance_in=balance_in, payment_day_in=payment_day_in,
                         monthly_payment_in=monthly_payment_in, payment_method_in=payment_method_in,
                         billing_type='Revolving Credit Bill', round_up=round_up_in)
        self.__apply_interest_date = 1
        self.append_trigger_day(self.__apply_interest_date)
        self.__apr_rate = apr_rate_in if apr_rate_in < 1 else round(apr_rate_in/100, 2)
        self.__interest_paid_to_date = 0
        self.__ledger = [['Date', 'Description', 'Credit', 'Debit', 'Balance', 'Interest To Date']]
        self.__credit_limit = credit_limit_in
        # The balance is technically debt
        self.set_balance(self.get_balance() * -1)

    # Method to apply the payment to the balance
    def make_payment(self, date_in):
        # If balance is more than payment we subtract it and return 0
        if abs(self.get_balance()) >= self.get_monthly_payment():
            # Apply payment to payment method
            self.payment_method.make_a_transaction(date_in=date_in, action=f'{self.get_bill_name()}-Payment', credit=0,
                                                   debit=self.get_monthly_payment())
            # Apply payment to ledger
            self.make_a_transaction(date_in=date_in, action='Payment', credit=self.get_monthly_payment(), debit=0)

        # If balance is less than payment we zero out the balance and return the difference ( to credit it back)
        elif self.get_balance() != 0:
            # Apply payment to payment method
            self.payment_method.make_a_transaction(date_in=date_in, action=f'{self.get_bill_name()}-Payment', credit=0,
                                                   debit=abs(self.get_balance()))
            # Apply payment to ledger
            self.make_a_transaction(date_in=date_in, action='Payoff Payment', credit=abs(self.get_balance()), debit=0)

    def calculate_interest(self, date_in):
        if abs(self.get_balance()) > 0:
            n_days = 365 if not is_leap(date_in.year) else 366
            interest = round((abs(self.get_balance())*(self.__apr_rate / n_days)), 2)
            self.__interest_paid_to_date += interest
            self.make_a_transaction(date_in=date_in, action='Daily Interest',
                                    credit=0, debit=interest)

    def __add_to_ledger(self, date_in, action, credit, debit):
        self.__ledger.append([date_in, action, round(credit, 2), round(debit, 2),
                              round(abs(self.get_balance()), 2), round(self.__interest_paid_to_date, 2)])

    def get_ledger(self):
        # mutable [] so we need to make a deep copy
        return deepcopy(self.__ledger)

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


if __name__ == '__main__':
    from datetime import date, timedelta

    primary_checking = BankAccount(account_name_in='Primary Checking', account_type_in='Checking', balance_in=2_500)
    primary_savings = BankAccount(account_name_in='Primary Savings', account_type_in='Savings', balance_in=500)
    primary_income = Income(name_in='Primary Job', income_in=2_300.00,
                            account_contributions_in=[(primary_checking, .9), (primary_savings, .1)],
                            initial_pay_date_in=date(2025, 8, 7),
                            payment_type_in=2)
    my_card = RevolvingCreditBill(name_in='Discovery', balance_in=20_000, payment_day_in=28,
                                  monthly_payment_in=800, apr_rate_in=.15, credit_limit_in=1_000,
                                  payment_method_in=primary_checking, round_up_in=False)

    today = date(2025, 1, 1)
    counter = 0
    while today < date(2027, 1, 1):
        # Check income First
        primary_income.process_day(date_in=today)

        # Check credit card
        if my_card.trigger_day(today.day):
            my_card.process_day(today)
        today += timedelta(days=1)

    print("Discovery Transactions!")
    for each in my_card.get_ledger():
        print(each)


