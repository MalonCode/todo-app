# VARIABLE + LIST: stores all our expenses
expenses = []
# IMPORT: brings in a built-in Python module for CSV files
import csv

# VARIABLE + LIST: stores all our expenses
expenses = []

# FUNCTION: saves all expenses to a file
def save_expenses():
    # OPEN FILE: creates or overwrites expenses.csv
    with open("expenses.csv", "w", newline="") as file:
        # VARIABLE + OBJECT: creates a csv writer
        writer = csv.DictWriter(file, fieldnames=["name", "amount", "category"])
        # METHOD: writes the header row
        writer.writeheader()
        # LOOP: writes each expense as a row
        for expense in expenses:
            writer.writerow(expense)

# FUNCTION: loads expenses from file when app starts
def load_expenses():
    # ERROR HANDLING: tries to open file, ignores if not found
    try:
        with open("expenses.csv", "r") as file:
            # VARIABLE + OBJECT: creates a csv reader
            reader = csv.DictReader(file)
            # LOOP: reads each row as a dictionary
            for row in reader:
                expenses.append({
                    "name": row["name"],           # STRING
                    "amount": float(row["amount"]), # FLOAT conversion
                    "category": row["category"]     # STRING
                })
    except:
        # KEYWORD: does nothing if file doesn't exist
        pass

# FUNCTION CALL: loads expenses when app starts
load_expenses()

# FUNCTION: displays the menu
def show_menu():
    print("================================")
    print("      EXPENSE TRACKER APP       ")
    print("================================")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. Delete an expense")
    print("5. Quit")
    print("================================")

# LOOP: keeps app running
while True:
    show_menu()
    
    # VARIABLE + STRING: stores user input
    choice = input("Enter your choice(1-5): ")
    
    # CONDITIONAL: checks what user picked
    if choice == "5":
        print("Goodbye!")
        break
   
    elif choice == "1":
        # VARIABLE + STRING: stores the expense name
        name = input("Enter expense name: ")
        
        # VARIABLE + FLOAT: stores decimal number for money
        amount = float(input("Enter amount spent: "))
        
        # VARIABLE + STRING: stores the category
        category = input("Enter category (Food/Transport/Bills/Other): ")
        
        # VARIABLE + DICTIONARY: groups all expense data together
        expense = {
            "name": name,          # STRING key: STRING value
            "amount": amount,      # STRING key: FLOAT value
            "category": category   # STRING key: STRING value
        }
        
        # LIST METHOD: adds dictionary to our list
        expenses.append(expense)
        
        # F-STRING: formatted confirmation message
        print(f"✓ {name} of ${amount} added successfully!")
    elif choice == "2":
        # CONDITIONAL: checks if list is empty
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            expenses.append(expense)
        save_expenses()  # FUNCTION CALL: saves after adding
        print("================================")
            print("       ALL YOUR EXPENSES        ")          print("================================")
            
            # LOOP + ENUMERATE: goes through each expense
            for i, expense in enumerate(expenses):
                # F-STRING: formats each expense neatly
                print(f"{i + 1}. {expense['name']}")
                print(f"   Amount:   ${expense['amount']}")
                print(f"   Category: {expense['category']}")
                print("--------------------------------")
    
    elif choice == "3":
        # CONDITIONAL: checks if list is empty
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            # VARIABLE + FLOAT: starts total at zero
            total = 0.0
            
            # LOOP: goes through every expense
            for expense in expenses:
                # ARITHMETIC: adds each amount to total
                total = total + expense["amount"]
            
            # DICTIONARY: groups spending by category
            categories = {}
            
            for expense in expenses:
                # VARIABLE + STRING: gets category name
                category = expense["category"]
                
                # CONDITIONAL: checks if category exists
                if category in categories:
                    categories[category] += expense["amount"]
                else:
                    categories[category] = expense["amount"]
            
            print("================================")
            print("         SPENDING SUMMARY       ")
            print("================================")
            
            # LOOP: goes through each category
            for category, amount in categories.items():
                # F-STRING: formats category total
                print(f"{category}: ${amount:.2f}")
            
            print("--------------------------------")
            # F-STRING + FLOAT: displays grand total
            print(f"TOTAL SPENT: ${total:.2f}")
            print("================================")
    elif choice == "4":
        # CONDITIONAL: checks if list is empty
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            print("================================")
            print("       DELETE AN EXPENSE        ")
            print("================================")
            
            # LOOP: shows all expenses with numbers
            for i, expense in enumerate(expenses):
                # F-STRING: displays each expense
                print(f"{i + 1}. {expense['name']} - ${expense['amount']:.2f}")
            
            # VARIABLE + INTEGER: gets which expense to delete
            number = int(input("Enter expense number to delete: "))
            
            # CONDITIONAL: checks if number is valid
            if number < 1 or number > len(expenses):
                print("Invalid number!")
            else:
                # VARIABLE + DICTIONARY: stores deleted expense
                deleted = expenses.pop(number - 1)
                
                # F-STRING: confirms deletion
                print(f"✓ {deleted['name']} deleted successfully!")
                deleted = expenses.pop(number - 1)
                save_expenses()  # FUNCTION CALL: saves after deleting