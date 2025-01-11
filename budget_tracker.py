import os
import json

class BudgetTracker:
    def __init__(self):
        self.data_file = "budget_data.json"
        self.budget = 0.0
        self.expenses = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.budget = data.get("budget", 0.0)
                self.expenses = data.get("expenses", [])

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump({"budget": self.budget, "expenses": self.expenses}, file)

    def set_budget(self):
        try:
            self.budget = float(input("Enter your budget for the month: $"))
            self.save_data()
            print(f"Budget set to ${self.budget:.2f}\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    def add_expense(self):
        try:
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: $"))
            self.expenses.append({"name": name, "amount": amount})
            self.save_data()
            print(f"Expense '{name}' of ${amount:.2f} added.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.\n")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return

        print("Your Expenses:")
        total_spent = 0.0
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")
            total_spent += expense['amount']
        print(f"Total Spent: ${total_spent:.2f}")
        print(f"Remaining Budget: ${self.budget - total_spent:.2f}\n")

    def check_budget(self):
        total_spent = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Spent: ${total_spent:.2f}")
        print(f"Budget: ${self.budget:.2f}")
        if total_spent > self.budget:
            print("Warning: You have exceeded your budget!\n")
        else:
            print("Good job! You are within your budget.\n")

    def menu(self):
        while True:
            print("Budget Tracker Menu")
            print("1. Set Budget")
            print("2. Add Expense")
            print("3. View Expenses")
            print("4. Check Budget")
            print("5. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.set_budget()
                elif choice == 2:
                    self.add_expense()
                elif choice == 3:
                    self.view_expenses()
                elif choice == 4:
                    self.check_budget()
                elif choice == 5:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.\n")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.menu()
