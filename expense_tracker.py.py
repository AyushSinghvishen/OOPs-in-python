class Expense:
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.category}: ₹{self.amount} ({self.description})"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print("✅ Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("⚠️ No expenses recorded yet.")
            return
        print("\n📒 Expense List:")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense}")

    def total_expense(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"\n💰 Total Expenses: ₹{total}")

    def category_wise_expense(self, category):
        filtered = [e for e in self.expenses if e.category.lower() == category.lower()]
        if not filtered:
            print(f"⚠️ No expenses found for category: {category}")
        else:
            print(f"\n📂 Expenses in {category}:")
            for e in filtered:
                print(e)


# ------------------- Running the Expense Tracker -------------------
def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (Food/Travel/Shopping/etc): ")
                description = input("Enter description (optional): ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("❌ Invalid amount! Please enter a number.")

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expense()

        elif choice == "4":
            category = input("Enter category name: ")
            tracker.category_wise_expense(category)

        elif choice == "5":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
