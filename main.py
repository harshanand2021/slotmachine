# importing modules
import random

# Declaring a constant
MAX_LINES = 5
MAX_BET = 10000 # Maximum bet amount
MIN_BET = 100 # Minimum bet amount

# Specifying the number of rows
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, 
    "B": 4, 
    "C": 6, 
    "D": 8
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
                    
    return winnings, winning_lines

def get_slot_machine_spin(rows,cols,sybmols):
    all_symbols = []
    for symbol, symbol_count in sybmols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])

# Function to deposit money
def deposit():
    while True:
        amount = input("What would you like to deposit? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if(amount > 0):
                break
            else :
                print("Please enter a valid amount.")
        else:
            print("Please enter a valid amount.")
            
    return amount

# Function to get the number of lines in a file
def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1 - " + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if(lines > 0):
                break
            else :
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a valid number of lines.")
            
    return lines

def getBet():
    while True:
        amount = input("What would you like to bet on each line? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else :
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
            
    return amount

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
                
        print()

# Main function
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(f"You don't have enough to bet on. Your balance is Rs.{balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet = Rs.{totalBet}")
    print("Balance: Rs.", balance, "Lines: ", lines)
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"You won {winnings}!")
    print(f"You won on lines : ", *winning_lines)

main()