def current_balance(transactions):
    income_balance = 0
    expenses_balance = 0
    income_balance = sum([income_balance+transaction["amount"] for transaction in transactions if transaction["type"] == "Income" ])
    expenses_balance = sum([expenses_balance+transaction["amount"] for transaction in transactions if transaction["type"] == "Expenses" ])
    return income_balance-expenses_balance

def total_income(transactions):
    income_balance = 0
    income_balance = sum([income_balance+transaction["amount"] for transaction in transactions if transaction["type"] == "Income" ])
    return income_balance

def total_expenses(transactions):
    expenses_balance = 0
    expenses_balance = sum([expenses_balance+transaction["amount"] for transaction in transactions if transaction["type"] == "Expenses" ])
    return expenses_balance
