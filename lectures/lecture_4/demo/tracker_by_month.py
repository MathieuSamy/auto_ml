from decimal import Decimal, getcontext
from datetime import datetime
from collections import defaultdict

getcontext().prec = 10
transactions = []
balance = Decimal('0.00')

def add_transaction(amount, description):
    global balance
    amount = Decimal(amount)
    date = datetime.now().strftime('%Y-%m-%d')
    transactions.append({'amount': amount, 'description': description, 'date': date})
    balance += amount
    print(f"Added transaction: ${amount:.2f} - {description} on {date}")
    print(f"New balance: ${balance:.2f}")

def expenses_by_month():
    monthly_expenses = defaultdict(Decimal)
    for t in transactions:
        if t['amount'] < 0:
            month = t['date'][:7]  # YYYY-MM
            monthly_expenses[month] += -t['amount']
    print("\nExpenses by Month:")
    for month, total in sorted(monthly_expenses.items()):
        print(f"{month}: ${total:.2f}")
    if not monthly_expenses:
        print("No expenses recorded.")

def main():
    print("Monthly Expense Tracker")
    print("Commands: add <amount> <description>, show, exit")
    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0] == "add" and len(parts) >= 3:
            amount = parts[1]
            description = " ".join(parts[2:])
            add_transaction(amount, description)
        elif parts[0] == "show":
            expenses_by_month()
        elif parts[0] == "exit":
            print("Exiting tracker.")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
