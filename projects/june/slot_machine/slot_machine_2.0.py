import random
import time

MAX_LINES = 3
MAX_BET = 1000000000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 5,
    "D": 7,
}

symbol_value = {
    "A": 50,
    "B": 10,
    "C": 5,
    "D": 2,
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

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
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
    print("╔═══════════╗")
    for row in range(len(columns[0])):
        print("║", end=" ")
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" ║ ")
            else:
                print(column[row], end=" ║")
        print()
    print("╚═══════════╝")

def animate_slot_machine():
    temp_symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for _ in range(20):  # number of animation frames
        columns = [[random.choice(temp_symbols) for _ in range(ROWS)] for _ in range(COLS)]
        print_slot_machine(columns)
        time.sleep(0.35)
        print("\033[F" * (ROWS + 2), end="")  # move cursor up to overwrite previous lines

def deposit():
    while True:
        amount = input("how much would you like to deposit? -->$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Amount must be a number.")
    print("═══════════════════════════════")

def get_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Enter a valid number of lines between 1 and {MAX_LINES}.")
        else:
            print("Enter a valid number.")
    print("═══════════════════════════════")
    

def get_bet():
    while True:
        amount = input(f"how much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Amount must be a number.")
    print("═══════════════════════════════")

def game(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"\nYou don't have enough money! Your current balance is ${balance}.")
        else:
            break
        
    print(f"\nYou are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

    print("\nSpinning the slot machine...\n")
    
    # Show animation before final result
    animate_slot_machine()

    # Final result
    columns = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(columns)
    winnings, winning_lines = check_winnings(columns, lines, bet, symbol_value)
    time.sleep(0.5)
    print(f"\n═══════════════════════════════")
    time.sleep(1)
    print(f"You won ${winnings}!")
    time.sleep(1)
    print(f"Winning lines:", *winning_lines)
    if winnings != 0:
        print("Wow, that's a lot of money! 🎉")
        print("Maybe you'll win more. Why not play again? 🙂")
    print("═══════════════════════════════\n")
    
    return balance + winnings - total_bet

def main():
    print("\n╔═════════════════════════════╗")
    print("║      WELCOME TO MY SLOT     ║")
    print("║         MACHINE GAME        ║")
    print("╚═════════════════════════════╝\n")
    time.sleep(2)
    
    print("\n╔═══════════════════════════════════════╗")
    print("║          info about the game:         ║")
    print("║       This game is totally fair!      ║")
    print("║    and you will win a lot of money!   ║")
    print("╚═══════════════════════════════════════╝\n")
    time.sleep(2)
    
    
    balance = deposit()
    while True:
        print(f"\n═══════════════════════════════")
        print(f"Current balance: ${balance}")
        print("═══════════════════════════════")
        
        
        if balance == 0:
            (f"\n═══════════════════════════════")
            print("\nyou ran out of money. Goodbye! :D hope to see you soon!!")
            (f"═══════════════════════════════")
            break
        
        spin = input("Press Enter to spin (q to quit): ")
        while spin.lower() != "q" and spin != "":
            spin = input("Press Enter to spin (q to quit): ")
        if spin.lower() == "q":
            break
        balance = game(balance)
    
    print("\n═══════════════════════════════")
    print(f"Final balance: ${balance}")
    print("Thank you for playing! Goodbye!")
    print("═══════════════════════════════\n")

main()