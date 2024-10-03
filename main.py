import argparse
from ast import arg
from data import load, save, export_to_csv
from datetime import datetime

# Crear el parser
parser = argparse.ArgumentParser(description="Expense Tracker CLI")

parser.add_argument("command", choices=["add", "remove", "update", "list", "summary", "delete", "clear", "export"])
parser.add_argument("-d","--description", help = "Create new expense", required = False)
parser.add_argument("-am","--amount", help = "Amount", required = False)
parser.add_argument("-c","--categorie", help = "Categirie", required = False)
parser.add_argument("-i","--id", help = "ID", required = False)
parser.add_argument("-m","--month", help = "Amount", required = False)
parser.add_argument("-nd","--new_description", help = "New Description", required = False)
parser.add_argument("-na","--new_amount", help = "New Amount", required = False)

args = parser.parse_args()

current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M")

expenses = load()

if args.command == 'add':
    if args.description and args.amount:
        try:
            expense_id = len(expenses) + 1
            new_expense = {
                "id": expense_id,
                "date": current_date,
                "time": current_time,
                "description": args.description,
                "amount": float(args.amount),
                "categorie": args.categorie if args.categorie else "Others"
            }
            expenses.append(new_expense)
            save(expenses)
            print(f"Expense added successfully with ID {expense_id}")
        except ValueError:
            print("Error: Amount must be a valid number.")
    else:
        print("Error: Description and amount are required.")

elif args.command == 'export':
    export_to_csv(expenses)


elif args.command == 'list':
    # Filtramos por categoría si está presente, si no, listamos todos los gastos
    filtered_expenses = [expense for expense in expenses if not args.categorie or expense.get('categorie') == args.categorie]

    if filtered_expenses:
        print("List of Expenses:" if not args.categorie else f"List of Expenses for category: {args.categorie}")
        for expense in filtered_expenses:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Categorie: {expense.get('categorie', 'others')}, Amount: {expense['amount']}, Date: {expense['date']}")
    else:
        print("No expenses found." if not args.categorie else f"No expenses found with categorie: {args.categorie}")


elif args.command == 'summary':
    if not expenses:
        print("Error: No expenses to summarize.")
    else:
        if args.month:
            try:
                month = int(args.month)
                total = sum(int(expense['amount']) for expense in expenses if datetime.strptime(expense['date'], "%Y-%m-%d").month == month)
            except ValueError:
                print("Error: Month must be a valid integer.")
        else:
            total = sum(float(expense['amount']) for expense in expenses)
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
            
elif args.command == 'clear':
    if expenses:
        expenses.clear()
        save(expenses)
        print("The expense list has been cleared.")
    else:
        print("No expenses to clear; the list is already empty.")

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

