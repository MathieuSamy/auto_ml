from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime
from decimal import Decimal, getcontext

getcontext().prec = 10
app = Flask(__name__)

transactions = []
balance = Decimal('0.00')

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Personal Finance Tracker</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 600px; margin: auto; }
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background: #eee; }
        .summary { margin-bottom: 20px; }
    </style>
</head>
<body>
<div class="container">
    <h1>Personal Finance Tracker</h1>
    <form method="post" action="/set_balance">
        <label>Set Balance: $</label>
        <input type="number" step="0.01" name="amount" required>
        <button type="submit">Set</button>
    </form>
    <form method="post" action="/add">
        <label>Amount: $</label>
        <input type="number" step="0.01" name="amount" required>
        <label>Description:</label>
        <input type="text" name="description" required>
        <button type="submit">Add Transaction</button>
    </form>
    <div class="summary">
        <h2>Summary</h2>
        <p>Total Income: ${{ income }}</p>
        <p>Total Expense: ${{ expense }}</p>
        <p>Current Balance: ${{ balance }}</p>
        <p>Number of transactions: {{ num_transactions }}</p>
        {% if transactions %}
        <p>First transaction: {{ transactions[0]['date'] }}</p>
        <p>Last transaction: {{ transactions[-1]['date'] }}</p>
        {% endif %}
    </div>
    <h2>Transaction History</h2>
    <table>
        <tr><th>#</th><th>Amount</th><th>Description</th><th>Type</th><th>Date</th></tr>
        {% for idx, t in enumerate(transactions, 1) %}
        <tr>
            <td>{{ idx }}</td>
            <td>${{ '%.2f'|format(t['amount']) }}</td>
            <td>{{ t['description'] }}</td>
            <td>{{ t['type'] }}</td>
            <td>{{ t['date'] }}</td>
        </tr>
        {% endfor %}
    </table>
</div>
</body>
</html>
'''

@app.route("/", methods=["GET"])
def index():
    income = sum(t['amount'] for t in transactions if t['amount'] > 0)
    expense = sum(-t['amount'] for t in transactions if t['amount'] < 0)
    return render_template_string(TEMPLATE,
        transactions=transactions,
        balance=f"{balance:.2f}",
        income=f"{income:.2f}",
        expense=f"{expense:.2f}",
        num_transactions=len(transactions)
    )

@app.route("/set_balance", methods=["POST"])
def set_balance_route():
    global balance
    amount = request.form['amount']
    balance = Decimal(amount)
    return redirect(url_for('index'))

@app.route("/add", methods=["POST"])
def add_transaction_route():
    global balance
    amount = Decimal(request.form['amount'])
    description = request.form['description']
    t_type = 'Income' if amount > 0 else 'Expense'
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transactions.append({'amount': amount, 'description': description, 'type': t_type, 'date': date})
    balance += amount
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
