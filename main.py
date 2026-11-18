from transactions.income import add_income
from transactions.expenses import expenses
from utils.calculations import (current_balance,total_income,total_expenses)
from utils.filters import (max_expenses, min_expenses)
from transactions.reports import generate_financial_report
from transactions.bank import (process_transactions,transaction_manager)
def display_menu():
    print("========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Financial Summary")
    print("5. Filter Transactions")
    print("6. Deposit Amount")
    print("7. Withdraw Amount")
    print("8. Exit")

transactions=[]
def main():
    bank = transaction_manager(20000)
    print(next(bank))
    while True:
        display_menu()
        choice = int(input("\n Enter your choise in between (1-8)"))
        match choice:
            case 1:
                print("Add Income Selected")
                if add_income() is not None:
                    transactions.append(add_income())
            case 2:
                print("Add Expense Selected ")
                if expenses() is not None:
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
                print("Deposit Selected")
                amount = int(input("Enter Deposit amount"))
                print(bank.send(amount))
            case 7:
                print("Withdraw Selected")
                amount = int(input("Enter Withdraw amount"))
                print(bank.send(amount))
            case 8:
                bank.close()
                print("Thank you for choosing PERSONAL EXPENSE TRACKER")
                break
            case _:
                print("Invalid Choice selected ")

if __name__ == "__main__":
    main()