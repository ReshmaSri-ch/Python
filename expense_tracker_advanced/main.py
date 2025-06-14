from tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense\n2. Show Summary\n3. Export CSV\n4. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            tracker.add_expense(amount, category, date)
        elif choice == '2':
            month = input("Month (MM or leave blank): ")
            year = input("Year (YYYY or leave blank): ")
            summary = tracker.get_summary(month if month else None, year if year else None)
            for cat, amt in summary:
                print(f"{cat}: ₹{amt}")
        elif choice == '3':
            tracker.export_to_csv()
        elif choice == '4':
            break