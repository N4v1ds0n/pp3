def get_cashflow_input():
    try:
        amount = float(input("Enter amount: £"))
        category = input("Enter category (e.g., food,...): ").lower()
        description = input("Optional description: ")
        return {"amount": amount, "category": category, "description": description}
    except ValueError:
        print("❌ Invalid input. Please enter a number for amount.")
        return get_cashflow_input()
