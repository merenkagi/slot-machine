import random                                        #we want to generate some random value for the slot machine

#lets define some values for the slot machine
ROWS  = 3                                            #rows
COLS = 3                                             #columns

#how many symbols are in each column
symbol_count = {                                     #declaring a dictionary 
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8 
}

# Define the payout values for each symbol
values = {
    "A": 5,
    "B": 10,
    "C": 15,
    "D": 20
}

#generate what the outcome of the slot machine was using the symbols
#generate what symbols are going to be in each column based on the frequency of symbols that we have
def get_slot_machine_spin(rows, cols, symbols):
    # Initialize an empty list to store all symbols based on their frequencies
    all_symbols = []

    # Iterate over each symbol and its count in the symbols dictionary
    for symbol, symbol_count in symbols.items():
        # Append the symbol to the list the number of times specified by its count
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Initialize an empty list to store the columns of the slot machine
    columns = [[] for _ in range(cols)]

    # Iterate over each column index
    for i in range(cols):
        # Make a copy of the all_symbols list to work with
        current_symbols = all_symbols[:]
        
        # Shuffle the symbols in the current_symbols list to randomize their order
        random.shuffle(current_symbols)

        # Iterate over each row in the column
        for _ in range(rows):
            # Pop a symbol from the current_symbols list and append it to the column
            value = current_symbols.pop()
            columns[i].append(value)

    # Return the generated columns of the slot machine
    return columns

def print_slot_machine(columns):
    # Iterate over each row index in the columns
    for row in range(len(columns[0])):
        # Iterate over each column index and its corresponding column
        for i, column in enumerate(columns):
            # Check if it's not the last column
            if i != len(columns) - 1:
                # Print the symbol with a separator "|"
                print(column[row], end=" | ")
            else:
                # Print the last symbol without a separator
                print(column[row], end="")
        
        # Move to the next line after printing each row
        print()