# Expenses Tracker

def add_expenses(expenses, amount, category):
    expenses.append({'Amount': amount, 'Category': category})

def list_all_expenses(expenses):
    for expense in expenses:
        print(f'Amount: Rs.{expense['Amount']}, Category: {expense['Category']}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['Amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return list(filter(lambda expense: expense['Category'] == category, expenses))

expenses = list()
print("Expenses tracker app")
while True:
    print("\nChoose your option:")
    print("1. Add an expense")
    print("2. List all expenses")
    print("3. Total expenses")
    print("4. Filter expenses by Category:")
    print("5. Exit\n")

    ch = input("Enter your choice:")

    if ch == '1':
        amount = float(input("Enter amount:"))
        category = input("Enter category:")
        add_expenses(expenses, amount, category)
        print("Details entered successfully.")
    elif ch == '2':
        print("List of all expenses:")
        list_all_expenses(expenses)
    elif ch == '3':
        print(f"Total expenses: Rs.{total_expenses(expenses)}.")
    elif ch == '4':
        category = input("Enter category to filter out expenses:")
        print(f"Expenses for {category}: {filter_expenses_by_category(expenses, category)}.")
    elif ch == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option! Please enter the valid choice.")