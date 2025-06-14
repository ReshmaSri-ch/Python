import tkinter as tk
from tkinter import messagebox
from tracker import ExpenseTracker

tracker = ExpenseTracker()

def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        date = date_entry.get()
        tracker.add_expense(amount, category, date)
        messagebox.showinfo("Success", "Expense added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def show_summary():
    summary = tracker.get_summary()
    result = ""
    for cat, amt in summary:
        result += f"{cat}: ₹{amt}\n"
    messagebox.showinfo("Summary", result)

def export_data():
    tracker.export_to_csv()
    messagebox.showinfo("Export", "Data exported to export.csv")

root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=2, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Show Summary", command=show_summary).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Export to CSV", command=export_data).grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()