from datetime import date, timedelta
from bank_account import *


def calculate_rounded_value(value_in, mod_value):
    value_in = int(value_in)
    if value_in % mod_value == 0:
        return value_in
    else:
        return value_in - (value_in % mod_value)


class Income:
    def __init__(self, name_in, income_in, account_contributions_in, initial_pay_date_in, payment_type_in,
                 round_down=False):
        self.__income_name = name_in
        self.__income_amount = 0
        self.set_income(income_in=income_in, round_down_in=round_down)
        self.__initial_pay_date = date(2025, 1, 1)
        self.set_inital_pay_date(initial_pay_date_in)
        self.__payment_type = payment_type_in if 1 <= payment_type_in <= 3 else 1
        '''
            1 = weekly pay
            2 = bi weekly pay
            3 = montly pay
        '''
        self.__account_contributions = account_contributions_in
        # [ (account_reference_1, percentage_1), account_reference_2, percentage_2) ..etc]

    def set_inital_pay_date(self, pay_date_in):
        if pay_date_in.day <= 28:
            self.__initial_pay_date = pay_date_in
        else:
            # if payment date is past the 28th we set it to 28th
            self.__initial_pay_date = date(year=pay_date_in.year, month=pay_date_in.month, day=28)

    def set_income(self, income_in, round_down_in):
        if not round_down_in:
            self.__income_amount = income_in
        else:
            # If we are grater than 1000
            if income_in >= 1000:
                self.__income_amount = calculate_rounded_value(income_in, 100)
            else:
                self.__income_amount = calculate_rounded_value(income_in, 10)

    def process_day(self, date_in):
        if self.trigger_income(date_in):
            # Make Account Contribution
            for account_refrence, contribution_percentage in self.__account_contributions:
                payment = round(self.__income_amount * contribution_percentage, 2)
                account_refrence.make_a_transaction(date_in=date_in, action=f'{self.__income_name}- Check',
                                                    credit=payment, debit=0)

    def trigger_income(self, date_in):
        # If we get paid monthly, lets see if we are in te
        if self.__payment_type == 3 and self.__initial_pay_date.day == date_in.day:
            return True
        # Bi weekly payment schedule
        elif self.__payment_type == 2 and abs(self.__initial_pay_date - date_in).days % 14 == 0:
            return True
        elif self.__payment_type == 1 and abs(self.__initial_pay_date - date_in).days % 7 == 0:
            return True
        return False


if __name__ == '__main__':
    primary_checking = BankAccount(account_name_in='Primary Checking', account_type_in='Checking', balance_in=0)
    secondary_checking = BankAccount(account_name_in='Secondary Checking', account_type_in='Checking', balance_in=0)

    primary_savings = BankAccount(account_name_in='Primary Savings', account_type_in='Savings', balance_in=0)
    secondary_savings = BankAccount(account_name_in='Secondary Savings', account_type_in='Savings', balance_in=0)

    contributions = [
        (primary_checking, .50),
        (secondary_checking, .1),
        (primary_savings, .3),
        (secondary_savings, .1)
    ]

    incomes = {
        Income(name_in='Primary Job', income_in=2_300.00,
               account_contributions_in=contributions, initial_pay_date_in=date(2025, 8, 7),
               payment_type_in=2),
        Income(name_in='Secondary Job', income_in=500.00,
               account_contributions_in=contributions, initial_pay_date_in=date(2025, 8, 7),
               payment_type_in=1)
    }

    today = date(2025, 1, 1)
    while today < date(2026, 1, 1):
        for income in incomes:
            income.process_day(date_in=today)
        today += timedelta(days=1)

    for bank, percentage in contributions:
        print(bank.get_account_name())
        for line in bank.get_ledger():
            print("\t", line)
