import sys
class InternalDecimal:
    def __init__(self, value):
        self.value = float(value)

    def __add__(self, other):
        return InternalDecimal(self.value + float(other))

    def __sub__(self, other):
        return InternalDecimal(self.value - float(other))

    def __gt__(self, other):
        return self.value > float(other)

    def __lt__(self, other):
        return self.value < float(other)

    def __neg__(self):
        return InternalDecimal(-self.value)

    def __float__(self):
        return self.value

    def __str__(self):
        return f"{self.value:.2f}"

    def __repr__(self):
        return f"InternalDecimal({self.value})"

def getcontext():
    class DummyContext:
        prec = 10
    return DummyContext()

Decimal = InternalDecimal
from datetime import datetime

getcontext().prec = 10

transactions = []
balance = Decimal('0.00')

def set_balance(amount):
    global balance
    balance = Decimal(amount)
    print(f"Balance set to ${balance:.2f}")

def add_transaction(amount, description):
    global balance
    amount = Decimal(amount)
    t_type = 'Income' if amount > 0 else 'Expense'
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transactions.append({'amount': amount, 'description': description, 'type': t_type, 'date': date})
    balance += amount
    print(f"Added transaction: ${amount:.2f} - {description} ({t_type}) on {date}")
    print(f"New balance: ${balance:.2f}")

def show_transactions():
    print("\nTransactions:")
    for idx, t in enumerate(transactions, 1):
        print(f"{idx}. ${t['amount']:.2f} - {t['description']} [{t['type']}] on {t['date']}")
    print(f"Current balance: ${balance:.2f}\n")

def show_history():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for idx, t in enumerate(transactions, 1):
            print(f"{idx}. ${t['amount']:.2f} - {t['description']} [{t['type']}] on {t['date']}")
    print(f"Current balance: ${balance:.2f}\n")

def summary():
    income = sum(t['amount'] for t in transactions if t['amount'] > 0)
    expense = sum(-t['amount'] for t in transactions if t['amount'] < 0)
    print(f"\nSummary:")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expense: ${expense:.2f}")
    print(f"Current Balance: ${balance:.2f}\n")
    print(f"Number of transactions: {len(transactions)}")
    if transactions:
        print(f"First transaction: {transactions[0]['date']}")
        print(f"Last transaction: {transactions[-1]['date']}")

def main():
    print("Personal Finance Tracker")
    print("Commands: set_balance <amount>, add <amount> <description>, show, summary, history, exit")
    while True:
        try:
            cmd = input("> ").strip()
            if not cmd:
                continue
            parts = cmd.split()
            if parts[0] == "set_balance" and len(parts) == 2:
                set_balance(parts[1])
            elif parts[0] == "add" and len(parts) >= 3:
                amount = parts[1]
                description = " ".join(parts[2:])
                add_transaction(amount, description)
            elif parts[0] == "show":
                show_transactions()
            elif parts[0] == "summary":
                summary()
            elif parts[0] == "history":
                show_history()
            elif parts[0] == "exit":
                print("Exiting tracker.")
                break
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"Error: {e}")

def delete_transaction(index):
    global balance
    if 0 <= index < len(transactions):
        t = transactions.pop(index)
        balance -= t['amount']
        print(f"Deleted transaction: ${t['amount']:.2f} - {t['description']}")
        print(f"New balance: ${balance:.2f}")
    else:
        print("Invalid transaction index.")

if __name__ == "__main__":
    main()