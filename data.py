import json
import os
import csv

FILE = "expenses.json"
CSV_FILE = "expenses.csv"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []

def save(e):
    with open(FILE, "w") as file:
        json.dump(e, file, indent=4)

def export_to_csv(expenses):#Obtiene como argumento una lista de gastos
    if not expenses:
        return False  # No hay gastos que exportar

    with open(CSV_FILE, 'w', newline = '') as csv_file:
        fieldnames = ['id', 'description', 'categorie', 'amount', 'date']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        writer.writeheader()  # Escribe los nombres de las columnas
        
        # Asegurarse de que cada gasto tenga las claves necesarias
        for expense in expenses:
            writer.writerow({
                'id': expense.get('id', ''),
                'description': expense.get('description', ''),
                'categorie': expense.get('categorie', 'others'),  # Valor predeterminado 'others' si falta la categoría
                'amount': expense.get('amount', ''),
                'date': expense.get('date', '')
            })
    
    return True  # Exportación exitosa