import csv
from database import get_connection

class ExpenseTracker:
    def __init__(self):
        self.conn = get_connection()

    def add_expense(self, amount, category, date):
        c = self.conn.cursor()
        c.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", (amount, category, date))
        self.conn.commit()

    def get_summary(self, month=None, year=None):
        c = self.conn.cursor()
        query = "SELECT category, SUM(amount) FROM expenses"
        conditions = []
        params = []

        if month:
            conditions.append("strftime('%m', date) = ?")
            params.append(f"{int(month):02d}")
        if year:
            conditions.append("strftime('%Y', date) = ?")
            params.append(str(year))

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " GROUP BY category"
        c.execute(query, params)
        return c.fetchall()

    def export_to_csv(self, filename='export.csv'):
        c = self.conn.cursor()
        c.execute("SELECT * FROM expenses")
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Amount', 'Category', 'Date'])
            writer.writerows(c.fetchall())
        print(f"Exported to {filename}")