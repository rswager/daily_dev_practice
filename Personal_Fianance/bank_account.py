from copy import deepcopy


class BankAccount:
    def __init__(self, account_name_in, account_type_in, balance_in):
        self.__balance = 0
        self.__account_name = account_name_in
        self.__account_type = account_type_in
        self.set_balance(balance_in=balance_in)
        self.__ledger = [['Date', 'Description', 'Credit', 'Debit', 'Balance']]

    def set_balance(self, balance_in):
        if balance_in >= 0:
            self.__balance = balance_in

    def get_balance(self):
        # immutable type double
        return self.__balance

    def get_account_name(self):
        # immutable type str
        return self.__account_name

    def get_account_type(self):
        # immutable type str
        return self.__account_type

    def make_a_transaction(self, date_in, action, credit, debit):
        self.set_balance(self.get_balance() + credit - debit)
        self.add_to_ledger(date_in=date_in, action=action, credit=credit, debit=debit)

    def add_to_ledger(self, date_in, action, credit, debit):
        self.__ledger.append([date_in, action, round(credit, 2), round(debit, 2), round(self.get_balance(), 2)])

    def get_ledger(self):
        # mutable [] so we need to make a deep copy
        return deepcopy(self.__ledger)
