import argparse
from data import load, save
from datetime import datetime

# Crear el parser
parser = argparse.ArgumentParser(description="Expense Tracker CLI")

parser.add_argument("command", choices=["add", "remove", "update"])
parser.add_argument("-d","--description", help = "Create new expense", required = False)
parser.add_argument("-am","--amount", help = "Amount", required = False)
parser.add_argument("-l","--list", action = "store_true", help = "List all expenses", required = False)

args = parser.parse_args()

current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M")

expenses = load()

if args.command == 'add':
    expense_id = len(expenses) + 1
    new_expense = {"id": expense_id, "date": current_date, "time": current_time, "description": args.description, "amount": args.amount }
    expenses.append(new_expense)
    save(expenses)
    print(f"Expense added successfully ID {expense_id}")
elif args.list:
    if expenses:
        print("List Expenses")
        for expense in expenses:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Fecha: {expense['date']}, Time: {expense['time']}")