def process_transactions(balance):
    try:
        while True:
            amount = yield f"Current Balance : ",balance
            if amount > 0:
                balance += amount
                print("Deposit amount : ",amount)
                print("Updated Balance : ",balance)
            elif abs(amount) <= balance and amount < 0:
                balance += amount
                print("Withdrawal amount : ",abs(amount))
                print("Updated Balance : ",balance)
            else:
                print("Enter Proper amount :")
    finally:
        print("Bank session closed successfully")

def transaction_manager(balance):
    yield from process_transactions(balance)

# bank = transaction_manager(20000)
# print(next(bank))
# amount = 5400
# print(bank.send(amount))
# amount = 500
# print(bank.send(amount))
# bank.close()