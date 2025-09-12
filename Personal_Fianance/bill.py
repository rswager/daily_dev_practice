from copy import deepcopy


def calculate_rounded_value(value_in, mod_value):
    value_in = int(value_in)
    if value_in % mod_value == 0:
        return value_in
    else:
        return value_in + (mod_value - (value_in % mod_value))


class Bill:
    def __init__(self, name_in, balance_in, payment_day_in,
                 monthly_payment_in, payment_method_in, billing_type='Default Bill', round_up=False):
        self.__balance = 0
        self.__bill_name = name_in
        self.__bill_type = billing_type
        self.set_balance(balance_in=balance_in)
        self.__monthly_payment = 0
        self.set_monthly_payment(monthly_payment_in=monthly_payment_in, round_up=round_up)
        self.__payment_day = 0
        self.set_payment_day(payment_day_in)
        self.__trigger_date = [self.__payment_day]
        self.payment_method = payment_method_in

    def set_balance(self, balance_in):
        self.__balance = balance_in

    def get_balance(self):
        # immutable type double
        return self.__balance

    def get_bill_name(self):
        # immutable type str
        return self.__bill_name

    def get_bill_type(self):
        # immutable type str
        return self.__bill_type

    def set_monthly_payment(self, monthly_payment_in, round_up):
        if not round_up:
            self.__monthly_payment = monthly_payment_in
        else:
            # If we are grater than 1000
            if monthly_payment_in >= 1000:
                self.__monthly_payment = calculate_rounded_value(monthly_payment_in, 100)
            else:
                self.__monthly_payment = calculate_rounded_value(monthly_payment_in, 10)

    def get_monthly_payment(self):
        # immutable type double
        return self.__monthly_payment

    # Take an integer in.
    # We will set the payment date to be between
    #   1 and 28, since February has only 28 Days
    #   If we get a number below 1 it goes to 1
    #   If we get a number bigger than 28 we set it to 28
    def set_payment_day(self, payment_day_in):
        if 1 <= payment_day_in <= 28:
            self.__payment_day = payment_day_in
        else:
            if payment_day_in < 1:
                self.__payment_day = 1
            else:
                self.__payment_day = 28

    # Return an integer representing the day of the month a bill is due
    def get_payment_day(self):
        # immutable type int
        return self.__payment_day

    def trigger_day(self, day_of_month_in):
        return day_of_month_in in self.__trigger_date

    def append_trigger_day(self, day_in):
        if day_in not in self.__trigger_date:
            self.__trigger_date.append(day_in)
