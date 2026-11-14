def max_expenses(transactions):
    expensive_transactions=[transaction for transaction in transactions if transaction["type"] == "Expenses"]
    return max(expensive_transactions ,key=lambda t: t["amount"])

def min_expenses(transactions):
    expensive_transactions=[transaction for transaction in transactions if transaction["type"] == "Expenses"]
    return min(expensive_transactions ,key=lambda t: t["amount"])