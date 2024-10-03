# Expense Tracker CLI 
[Link to Roadmap proyect](https://roadmap.sh/projects/expense-tracker)

Expense Tracker CLI is a command-line interface (CLI) tool designed to help users manage and track their daily expenses efficiently. This tool allows users to add, list, update, delete, and export expenses, providing a simple yet powerful way to keep track of personal finances.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Add a New Expense](#add-a-new-expense)
  - [List Expenses](#list-expenses)
  - [Update an Expense](#update-an-expense)
  - [Delete an Expense](#delete-an-expense)
  - [Clear All Expenses](#clear-all-expenses)
  - [Export Expenses to CSV](#export-expenses-to-csv)
  - [Summary of Expenses](#summary-of-expenses)
- [Project Structure](#project-structure)

## Features

- **Add a New Expense:** Record a new expense with a description, amount, category, date, and time.
- **List Expenses:** View all recorded expenses or filter them by category.
- **Update an Expense:** Modify the description and/or amount of an existing expense using its ID.
- **Delete an Expense:** Remove a specific expense from the records using its ID.
- **Clear All Expenses:** Remove all recorded expenses at once.
- **Export to CSV:** Export your expenses to a CSV file for further analysis or record-keeping.
- **Summary of Expenses:** Get a total summary of your expenses, optionally filtered by month.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/leonardoriveromatos/Expense-Tracker.git
   cd expense-tracker-cli
   ```

2. **Ensure You Have Python Installed:**

   This project requires Python 3.x. You can check your Python version with:

   ```bash
   python --version
   ```

   If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

## Usage

The Expense Tracker CLI is operated via the command line. Below are the commands and options available.

### Add a New Expense

Add a new expense by providing a description and amount. Optionally, you can specify a category.

```bash
python main.py add -d "Groceries" -am 50 -c "Food"
```

- `add`: Command to add a new expense.
- `-d` or `--description`: Description of the expense.
- `-am` or `--amount`: Amount of the expense.
- `-c` or `--categorie`: Category of the expense (optional). If not provided, defaults to "Others".

### List Expenses

List all recorded expenses.

```bash
python main.py list
```

List expenses filtered by a specific category.

```bash
python main.py list -c "Food"
```

- `list`: Command to list expenses.
- `-c` or `--categorie`: Category to filter expenses (optional).

### Update an Expense

Update the description and/or amount of an existing expense by specifying its ID.

```bash
python main.py update -i 2 -nd "Supermarket Groceries" -na 60
```

- `update`: Command to update an expense.
- `-i` or `--id`: ID of the expense to update.
- `-nd` or `--new_description`: New description for the expense (optional).
- `-na` or `--new_amount`: New amount for the expense (optional).

### Delete an Expense

Delete a specific expense by its ID.

```bash
python main.py delete -i 3
```

- `delete`: Command to delete an expense.
- `-i` or `--id`: ID of the expense to delete.

### Clear All Expenses

Remove all recorded expenses at once.

```bash
python main.py clear
```

- `clear`: Command to clear all expenses.

### Export Expenses to CSV

Export all expenses to a CSV file named `expenses.csv`.

```bash
python main.py export
```

- `export`: Command to export expenses to CSV.

### Summary of Expenses

Get a summary of your total expenses. Optionally, you can filter the summary by month.

```bash
python main.py summary
```

```bash
python main.py summary -m 10
```

- `summary`: Command to get a summary of expenses.
- `-m` or `--month`: Month number (1-12) to filter the summary (optional).

## Project Structure

```plaintext
expense-tracker-cli/
├── data.py
├── main.py
├── expenses.json
├── expenses.csv
├── README.md
```

