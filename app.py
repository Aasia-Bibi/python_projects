from flask import Flask, render_template, request, redirect, url_for
from budget_tracker import BudgetTracker  # Import your existing logic

app = Flask(__name__)
tracker = BudgetTracker()  # Initialize the tracker

@app.route('/')
def index():
    return render_template('index.html', budget=tracker.budget)

@app.route('/set_budget', methods=['POST'])
def set_budget():
    budget = request.form.get('budget')
    try:
        tracker.budget = float(budget)
        tracker.save_data()
    except ValueError:
        pass
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    name = request.form.get('name')
    amount = request.form.get('amount')
    try:
        tracker.expenses.append({'name': name, 'amount': float(amount)})
        tracker.save_data()
    except ValueError:
        pass
    return redirect(url_for('view_expenses'))

@app.route('/view_expenses')
def view_expenses():
    total_spent = sum(expense['amount'] for expense in tracker.expenses)
    remaining_budget = tracker.budget - total_spent
    return render_template('expenses.html', expenses=tracker.expenses, total_spent=total_spent, remaining_budget=remaining_budget)

if __name__ == '__main__':
    app.run(debug=True)
