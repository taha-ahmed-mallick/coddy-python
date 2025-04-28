print("Welcome to the Daily Expense Tracker!")
print(
    """
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit"""
)

expenses = []

while True:
    choice = int(input())
    if choice == 1:
        expense = float(input())
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == 2:
        if len(expenses) != 0:
            print("Your expenses:")
            for i, expense in enumerate(expenses):
                print(f"{i+1}. {expense}")
        else:
            print("No expenses recorded yet.")
    elif choice == 3:
        if len(expenses) != 0:
            summation = sum(expenses)
            avg = summation / len(expenses)
            print(f"Total expense: {summation}")
            print(f"Average expense: {avg}")
        else:
            print("No expenses recorded yet.")
    elif choice == 4:
        expenses.clear()
        print("All expenses cleared.")
    elif choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
