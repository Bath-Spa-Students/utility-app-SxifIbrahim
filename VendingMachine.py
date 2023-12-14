from rich.console import Console
from rich.table import Table
from rich.text import Text
import random

console = Console()

text_to_center ="""
█░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄
"""
terminal_width = console.width
centered_text = Text(text_to_center.center(terminal_width))

# Dictionary
data = {
    'A1': {'category': 'Snacks', 'item': 'Lays', 'price': 2.95, 'stock': 5},    
    'A2': {'category': 'Snacks', 'item': 'Pringles', 'price': 4.75, 'stock': 8},
    'B1': {'category': 'Snacks', 'item': 'Piattos', 'price': 9.95, 'stock': 3},
    'B2': {'category': 'Snacks', 'item': 'Chippy', 'price': 3.25, 'stock': 6},
    'C1': {'category': 'Snacks', 'item': 'Pillows', 'price': 5.50, 'stock': 3},
    'C2': {'category': 'Drinks', 'item': 'Water', 'price': 1.00, 'stock': 2},
    'D1': {'category': 'Drinks', 'item': 'Pepsi', 'price': 2.00, 'stock': 4},
    'D2': {'category': 'Drinks', 'item': 'Coke', 'price': 2.00, 'stock': 5},
    'E1': {'category': 'Drinks', 'item': 'Sprite', 'price': 2.00, 'stock': 2},
    'E2': {'category': 'Drinks', 'item': 'Mountain Dew', 'price': 2.00, 'stock': 7},
}

# Table
def display_table():
    table = Table()


    table.add_column("Code", justify='center', style='green1')
    table.add_column("Category", justify='center', style='green1')
    table.add_column("Item", justify='center', style='green1')
    table.add_column("Price", justify='center', style='green1')
    table.add_column("Stock", justify='center', style='green1')

    for code, details in data.items():
        stock_style = "red" if details['stock'] < 5 else "green1"
        table.add_row(
            code,
            details['category'],
            details['item'],
            f"AED {details['price']:.2f}",
            f"[{stock_style}]{details['stock']}[/{stock_style}]"
        )

# Prints the title and the table
    console = Console()
    console.print(text_to_center, style='cyan', justify='center')
    console.print(table, justify='center')

# Display the table
display_table()

total_money_inserted = 0
try:
    money_inserted = float(input("Insert money (press 0 to exit): AED "))
    if money_inserted < 0:
        print("Please enter a positive amount.")
    elif money_inserted == 0:
        print("No money inserted. Exiting...")
    else:
        total_money_inserted += money_inserted
        print(f"Money inserted: AED {money_inserted:.2f}")
        print(f"Total money inserted: AED {total_money_inserted:.2f}")

        # Rest of your code after money insertion
        # ...

        while True:
            try:
                # Display the table again
                display_table()

                # Ask for the code for the item
                code_to_buy = input("Enter the code of the item you want to buy: ").upper()

                if code_to_buy in data:
                    if data[code_to_buy]['stock'] > 0:
                        print(f"Dispensing {data[code_to_buy]['item']}...")
                        data[code_to_buy]['stock'] -= 1

                        total_money_inserted -= data[code_to_buy]['price']

                        # Suggest a random item from a different category
                        purchased_category = data[code_to_buy]['category']
                        available_categories = {details['category'] for code, details in data.items() if details['stock'] > 0 and details['category'] != purchased_category}

                        if available_categories:
                            suggested_category = random.choice(list(available_categories))
                            suggested_items = [
                                details['item'] for code, details in data.items()
                                if details['category'] == suggested_category and details['stock'] > 0
                            ]

                            if suggested_items:
                                suggested_item = random.choice(suggested_items)
                                print(f"Suggestion: You might also like {suggested_item}.")
                        elif not any(details['stock'] > 0 for code, details in data.items() if details['category'] != purchased_category):
                            print("No other items available in different categories.")
                    elif data[code_to_buy]['stock'] == 0:
                        print("Sorry, this item is out of stock.")
                    else:
                        print("Insufficient funds.")
                else:
                    print("Invalid code. Please enter a valid code.")

                # Display the table after the transaction
                display_table()

                # Dispense change
                if total_money_inserted >= data[code_to_buy]['price']:
                    print(f"Change: ${total_money_inserted:.2f}")
                else:
                    print("Insufficient funds. No change will be dispensed.")

                # Ask if the user wants to add more money
                add_more_money = input("Do you want to add more money? (y/n): ").lower()
                if add_more_money == 'y':
                    try:
                        additional_money = float(input("Insert money (press 0 to exit): AED "))
                        if money_inserted == 0:
                            break
                        total_money_inserted += additional_money
                    except ValueError:
                        print("Invalid input. Please enter a valid amount.")

            # Ask if the user wants to make another purchase
                another_purchase = input("Do you want to make another purchase? (y/n): ").lower()
                if another_purchase != 'y':
                    break

            except ValueError:
                print("Invalid input. Please enter a valid code or amount.")

except ValueError:
    print("Invalid input. Please enter a valid amount.")