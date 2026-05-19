import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class ExpenseTracker:

    def __init__(self, file_name="expenses.csv"):
        self.file_name = file_name

        # If CSV exists → load, else create new
        if os.path.exists(self.file_name):
            self.df = pd.read_csv(self.file_name)
        else:
            self.df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
            self.df.to_csv(self.file_name, index=False)

    # -------------------------
    # 1. ADD NEW EXPENSE
    # -------------------------
    
    def add_expense(self, date, amount, category, description):

        # INPUT VALIDATION
        try:
            amount = float(amount)
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
        except:
            print("❌ Invalid amount!")
            return

        if not isinstance(category, str) or category.strip() == "":
            print("❌ Invalid category!")
            return

        # append new record
        new_row = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.df.to_csv(self.file_name, index=False)

        print("✅ Expense added successfully!")

    # -------------------------
    # 2. SUMMARY (TOTAL, AVERAGE, CATEGORY WISE)
    # -------------------------

    def get_summary(self):
        if self.df.empty:
            print("⚠ No expense data found!")
            return

        total = np.sum(self.df["Amount"])
        avg = np.mean(self.df["Amount"])
        category_total = self.df.groupby("Category")["Amount"].sum()

        print("\n📊 EXPENSE SUMMARY")
        print("--------------------")
        print(f"Total Spending: ₹{total}")
        print(f"Average Spending: ₹{avg:.2f}")

        print("\nCategory-wise Total:")
        print(category_total)

    # -------------------------
    # 3. FILTER EXPENSES
    # -------------------------

    def filter_expenses(self, category=None, start_date=None, end_date=None):

        if self.df.empty:
            print("⚠ No data to filter!")
            return

        filtered = self.df.copy()

        if category:
            filtered = filtered[filtered["Category"] == category]

        if start_date and end_date:
            filtered = filtered[
                (filtered["Date"] >= start_date) &
                (filtered["Date"] <= end_date)
            ]

        print("\n📌 FILTERED DATA:")
        print(filtered)

        return filtered

    # -------------------------
    # 4. VISUALIZATIONS
    # -------------------------

    def plot_charts(self):
        if self.df.empty:
            print("⚠ No data for charts!")
            return

        # BAR CHART
        plt.figure(figsize=(7, 5))
        self.df.groupby("Category")["Amount"].sum().plot(kind="bar")
        plt.title("Total Expenses by Category")
        plt.ylabel("Amount")
        plt.xlabel("Category")
        plt.show()

        # LINE GRAPH
        plt.figure(figsize=(7, 5))
        daily = self.df.groupby("Date")["Amount"].sum()
        daily.plot(kind="line")
        plt.title("Daily Spending Trend")
        plt.ylabel("Amount")
        plt.xlabel("Date")
        plt.xticks(rotation=45)
        plt.show()

        # PIE CHART
        plt.figure(figsize=(6, 6))
        self.df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Category Spending Percentage")
        plt.show()

        # HISTOGRAM
        plt.figure(figsize=(7, 5))
        sns.histplot(self.df["Amount"], bins=10)
        plt.title("Expense Amount Distribution")
        plt.xlabel("Amount")
        plt.show()


# ==========================================
# MAIN MENU FOR USER INTERACTION
# ==========================================

def main():
    tracker = ExpenseTracker()

    while True:

        '''============================================'''
        print("\n======= SMART EXPENSE TRACKER =======")
        print("1. Add New Expense")
        print("2. View Summary")
        print("3. Filter Expenses")
        print("4. Show Visual Charts")
        print("5. Exit")
        '''============================================'''

        choice = input("Enter choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")

            tracker.add_expense(date, amount, category, description)

        elif choice == "2":
            tracker.get_summary()

        elif choice == "3":
            cat = input("Filter by category (enter to skip): ")
            sd = input("Start date YYYY-MM-DD (enter to skip): ")
            ed = input("End date YYYY-MM-DD (enter to skip): ")
            tracker.filter_expenses(cat if cat else None,
                                    sd if sd else None,
                                    ed if ed else None)

        elif choice == "4":
            tracker.plot_charts()

        elif choice == "5":
            print("👍 Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
