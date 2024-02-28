import json
import os
from collections import defaultdict
from datetime import datetime

# Function to load expense data from file
def load_expenses():
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as f:
            return json.load(f)
    else:
        return defaultdict(list)

# Function to save expense data to file
def save_expenses(expenses):
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

# Function to add a new expense
def add_expense(expenses, category, amount, description):
    today = datetime.today().strftime('%Y-%m-%d')
    expenses[today].append({'category': category, 'amount': amount, 'description': description})

# Function to view monthly expenses summary
def view_monthly_summary(expenses):
    monthly_summary = defaultdict(float)
    for date, items in expenses.items():
        month = date[:7]
        for item in items:
            monthly_summary[month] += item['amount']
    
    for month, total in monthly_summary.items():
        print(f'{month}: ${total:.2f}')

# Function to view category-wise expenditure
def view_category_summary(expenses):
    category_summary = defaultdict(float)
    for items in expenses.values():
        for item in items:
            category_summary[item['category']] += item['amount']
    
    for category, total in category_summary.items():
        print(f'{category}: ${total:.2f}')

# Function to handle user interaction
def main():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter amount spent: "))
            description = input("Enter description: ")
            add_expense(expenses, category, amount, description)
            save_expenses(expenses)
            print("Expense added successfully!")
        
        elif choice == '2':
            view_monthly_summary(expenses)
        
        elif choice == '3':
            view_category_summary(expenses)
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
