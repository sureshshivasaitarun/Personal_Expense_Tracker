from transactions.income import add_income
from transactions.expenses import expenses
from utils.calculations import (current_balance,total_income,total_expenses)
from utils.filters import (max_expenses, min_expenses)
from transactions.reports import generate_financial_report
def display_menu():
    print("========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Financial Summary")
    print("5. Filter Transactions")
    print("6. Exit")

transactions=[]
def main():
    while True:
        display_menu()
        choice = int(input("\n Enter your choise in between (1-6)"))
        match choice:
            case 1:
                print("Add Income Selected")
                transactions.append(add_income())
            case 2:
                print("Add Expense Selected ")
                transactions.append(expenses())
            case 3:
                print("View Transactions Selected")
                for i in range(len(transactions)):
                    print(f"Transaction {i+1}: {transactions[i]}")
            case 4:
                print("Financial Summary Selected")
                generate_financial_report(transactions)
                # print(f"This Month Total Income is: {total_income(transactions)}")
                # print(f"This Month Total Expenses is: {total_expenses(transactions)}")
                # print(f"Current Available Balance is: {current_balance(transactions)}")

            case 5:
                print("Filter Transactions selected")
                print(f"maximum expenses is {max_expenses(transactions)}")
                print(f"minimum expenses is {min_expenses(transactions)}")

            case 6:
                print("Thank you for choosing PERSONAL EXPENSE TRACKER")
                break
            case _:
                print("Invalid Choice selected ")

if __name__ == "__main__":
    main()