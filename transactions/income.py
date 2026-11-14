def add_income():
    print("\n========== ADD INCOME ==========")
    source=input("Enter Income Source :")
    amount=float(input("Enter Income Amount :"))
    description=input("Enter description :")
    income = {
        "type": "Income",
        "source": source,
        "amount": amount,
        "description": description
    }

    print("Income added Sucessfully!")
    print(income)
    return income