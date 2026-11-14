from utils.calculations import (current_balance,total_income,total_expenses)
from utils.filters import (max_expenses,min_expenses)

def generate_financial_report(transactions):
    print(f"Total Income {total_income(transactions)}")
    print(f"Total Expenses {total_expenses(transactions)}")
    print(f"Current Balance {current_balance(transactions)}")
    print(f"Maximum Expenses {max_expenses(transactions)}")
    print(f"Minimum Expenses {min_expenses(transactions)}")
