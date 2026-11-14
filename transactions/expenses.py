def expenses():
    print("\nEnter your Expenses here :")
    source = input("Enter the source of your expences :")
    amount = float(input("Enter how much its cost :"))
    description = input("Enter description :")

    expenses = {
        "type" : "Expenses",
        "source": source,
        "amount": amount,
        "description": description
    }
    print(expenses)
    return expenses