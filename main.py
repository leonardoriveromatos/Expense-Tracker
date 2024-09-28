import argparse
from data import load, save
from datetime import datetime

# Crear el parser
parser = argparse.ArgumentParser(description="Expense Tracker CLI")

parser.add_argument("command", choices=["add", "remove", "update", "list", "summary", "delete"])
parser.add_argument("-d","--description", help = "Create new expense", required = False)
parser.add_argument("-am","--amount", help = "Amount", required = False)
parser.add_argument("-i","--id", help = "ID", required = False)
parser.add_argument("-m","--month", help = "Amount", required = False)
parser.add_argument("-nd","--new_description", help = "New Description", required = False)
parser.add_argument("-na","--new_amount", help = "New Amount", required = False)


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
elif args.command == 'list':
    if expenses:
        print("List Expenses")
        for expense in expenses:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Fecha: {expense['date']}, Time: {expense['time']}")
elif args.command == 'summary':
    if expenses and args.month:
        month = int(args.month)
        total = sum(int(expense['amount']) for expense in expenses if datetime.strptime(expense['date'], "%Y-%m-%d").month == month)
    elif expenses:
        total = sum(int(expense['amount']) for expense in expenses)
    print(f"Total expenses: {total}")

elif args.command == 'delete':
    if not args.id:
        print("Error: You must provide an ID to delete an expense.")
    else:
        try:
            expense_to_remove = next(expense for expense in expenses if expense['id'] == int(args.id))
        except StopIteration:
            print(f"Error: Expense with ID {args.id} not found.")
        else:
            expenses.remove(expense_to_remove)
            save(expenses)
            print("Expense deleted successfully")    

elif args.command == 'update':
    if not args.id:
        print("Error: You must provide an ID to update an expense.")
    else:
        try:
            expense = next(exp for exp in expenses if exp['id'] == int(args.id))
        except StopIteration:
            print(f"Error: Expense with ID {args.id} not found.")
        else:
            if args.new_description:
                expense['description'] = args.new_description

            if args.new_amount:
                try:
                    expense['amount'] = float(args.new_amount)
                except ValueError:
                    print("Error: The amount must be a valid number.")
            save(expenses)
            print("Updated successfully")
