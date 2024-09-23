import argparse
from data import load_expenses,save_expenses

# Crear el parser
parser = argparse.ArgumentParser(description="Expense Tracker CLI")

parser.add_argument("-a","--add", help = "Create new expense", required = False)

args = parser.parse_args()

if args.add:
    print("Gasto añadido")