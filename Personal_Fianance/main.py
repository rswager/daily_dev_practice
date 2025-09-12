# Developed Objects
from financed_bill import *
from recurring_bill import *
from revolving_credit_bill import *
from income import *
from bank_account import *

# Imported Libraries
from datetime import date, timedelta
import xlsxwriter


def get_col(col_num_in):
    col = ['A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

    if col_num_in < 26:
        return col[col_num_in]
    elif col_num_in > 701:
        return False
    else:
        factor = int(col_num_in / 26) - 1
        remain = (col_num_in % 26)
        return str(col[factor]) + str(col[remain])


def add_table(worksheet_in, table_name_in, data_in):
    data = data_in
    header_in = data.pop(0)
    header = []
    for column in header_in:

        if column in ['Credit', 'Debit', 'Balance', 'Interest To Date']:
            column_def = {'header': column, 'format': accounting_format}
        elif column in ['Date']:
            column_def = {'header': column, 'format': date_format}
        else:
            column_def = {'header': column}

        header.append(column_def)

    worksheet_in.add_table(f'A1:{get_col(len(header)-1)}{len(data)+1}', {
        'header_row': True,
        'data': data,
        'total_row': False, 'autofilter': True,
        'columns': header, 'style': "Table Style Medium 9",
        'name': f'{str(table_name_in)}_Table'
    })


def add_chart(workbook_in, worksheet_in, table_name_in):
    chart = workbook_in.add_chart({'type': 'line'})
    chart.add_series({
        'categories': f'{table_name_in}_Table[Date]',
        'values': f'{table_name_in}_Table[Balance]',
        'name': 'Projected Balance'
    })

    worksheet_in.insert_chart('H1', chart, {'x_scale': 2.5, 'y_scale': 2.5})


# Frequency Codes
WEEKLY = 1
BI_WEEKLY = 2
MONTHLY = 3

# Round Up Down Flag
# True = Round Up Bills, Round Down Income
# False = Bills and Income
round_up_down = False

# Start and End Dates for Simulation
today = date(2025, 8, 1)
end_date = date(2032, 8, 1)

accounts = {
    'primary_checking': BankAccount(account_name_in='Primary Checking', account_type_in='Checking', balance_in=1_000),
    'primary_savings': BankAccount(account_name_in='Primary Savings', account_type_in='Savings', balance_in=1_500)
}

incomes = {
    'primary_income': Income(name_in='Primary Job', income_in=2_557.31,
                             account_contributions_in=
                             [
                                 (accounts['primary_checking'], .9),  # 90% to primary checking
                                 (accounts['primary_savings'], .1)  # 10% to primary savings
                             ],
                             initial_pay_date_in=date(2025, 8, 7), payment_type_in=BI_WEEKLY, round_down=round_up_down)
}

revolving_credit = {
    'discover_card': RevolvingCreditBill(name_in='Discovery', balance_in=30, payment_day_in=28,
                                         monthly_payment_in=500, apr_rate_in=.15, credit_limit_in=1_500,
                                         payment_method_in=accounts['primary_checking'], round_up_in=round_up_down)
}

bills = {
    'Mortgage': FinancedBill(name_in='Mortgage', balance_in=140_000.00, payment_day_in=1, monthly_payment_in=1_876.00,
                             payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'Car Payment - Ford': FinancedBill(name_in='Car Payment - Ford', balance_in=28_000.00, payment_day_in=15,
                                       monthly_payment_in=450.00,
                                       payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'Student Loans': FinancedBill(name_in='Student Loans', balance_in=35_000.00, payment_day_in=30,
                                  monthly_payment_in=461.00, payment_method_in=accounts['primary_checking'],
                                  round_up_in=round_up_down),

    'Car Insurance': RecurringBill(name_in='Car Insurance', balance_in=0, initial_payment_date_in=date(2025, 8, 16),
                                   recurring_type_in=MONTHLY, monthly_payment_in=300.00,
                                   payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'Netflix': RecurringBill(name_in='Netflix', balance_in=0, initial_payment_date_in=date(2025, 8, 9),
                             recurring_type_in=MONTHLY, monthly_payment_in=12.99,
                             payment_method_in=revolving_credit['discover_card'], round_up_in=round_up_down),

    'XboxLive': RecurringBill(name_in='XboxLive', balance_in=0, initial_payment_date_in=date(2025, 8, 3),
                              recurring_type_in=MONTHLY, monthly_payment_in=12.99,
                              payment_method_in=revolving_credit['discover_card'], round_up_in=round_up_down),


    'Internet': RecurringBill(name_in='Internet', balance_in=0, initial_payment_date_in=date(2025, 8, 3),
                              recurring_type_in=MONTHLY, monthly_payment_in=59.99,
                              payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'Utilities': RecurringBill(name_in='Utilities', balance_in=0, initial_payment_date_in=date(2025, 8, 1),
                               recurring_type_in=MONTHLY, monthly_payment_in=300.00,
                               payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'ADT': RecurringBill(name_in='ADT', balance_in=0, initial_payment_date_in=date(2025, 8, 15),
                         recurring_type_in=MONTHLY, monthly_payment_in=50.00,
                         payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'Food': RecurringBill(name_in='Food', balance_in=0, initial_payment_date_in=date(2025, 8, 1),
                          recurring_type_in=WEEKLY, monthly_payment_in=75.00,
                          payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'Fun': RecurringBill(name_in='Fun', balance_in=0, initial_payment_date_in=date(2025, 8, 1),
                         recurring_type_in=WEEKLY, monthly_payment_in=50.00,
                         payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'Gas': RecurringBill(name_in='Gas', balance_in=0, initial_payment_date_in=date(2025, 8, 1),
                         recurring_type_in=WEEKLY, monthly_payment_in=10.00,
                         payment_method_in=accounts['primary_checking'], round_up_in=round_up_down),

    'Therapy': RecurringBill(name_in='Therapy', balance_in=0, initial_payment_date_in=date(2025, 8, 8),
                             recurring_type_in=BI_WEEKLY, monthly_payment_in=30.00,
                             payment_method_in=accounts['primary_checking'], round_up_in=round_up_down)
}

# Walk Through Each day until we reach last day
while today < end_date:

    # process income
    for income in incomes:
        incomes[income].process_day(today)

    # Process bills
    for bill in bills:
        bills[bill].process_day(today)

    # Process revolving credit
    for credit in revolving_credit:
        revolving_credit[credit].process_day(today)

    today += timedelta(days=1)

workbook = xlsxwriter.Workbook('Output_Analysis.xlsx')
accounting_format = workbook.add_format({'num_format': 44})
date_format = workbook.add_format({'num_format': 14})
for each in accounts:
    worksheet = workbook.add_worksheet(f'{each}_Table')
    add_table(worksheet_in=worksheet, table_name_in=each, data_in=accounts[each].get_ledger())
    add_chart(workbook_in=workbook, worksheet_in=worksheet, table_name_in=each)


for each in revolving_credit:
    worksheet = workbook.add_worksheet(f'{each}_Table')
    add_table(worksheet_in=worksheet, table_name_in=each, data_in=revolving_credit[each].get_ledger())
    add_chart(workbook_in=workbook, worksheet_in=worksheet, table_name_in=each)

workbook.close()
