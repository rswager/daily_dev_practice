from accountInformation import AccountInformation
from datetime import date
from enumType import AccountType
from ledger import Ledger

class BankAccount:
    def __init__(self, name_in: str, balance_in: float, account_type_in: AccountType) -> None:
        self._accountInfo = AccountInformation(name_in, balance_in, account_type_in)
        self._ledger = Ledger(columns=['No.', 'Date', 'Description', 'Credit', 'Debit', 'Balance'])

    @property
    def ledger(self) -> list:
        # returns a deep copy of the ledger
        return self._ledger.ledger

    @property
    def ledger_col_count(self) -> int:
        return self._ledger.col_count

    @property
    def account_name(self) -> str:
        return self._accountInfo.account_name

    @property
    def account_type(self) -> AccountType:
        return self._accountInfo.account_type

    def make_a_transaction(self, date_in: date, action: str, credit: float, debit: float):
        self._accountInfo.update_balance(credit=credit,debit=debit)
        self._ledger.add_entry_to_ledger([self._ledger.row_number, date_in, action,round(credit,2),round(debit,2), round(self._accountInfo.balance,2)])
