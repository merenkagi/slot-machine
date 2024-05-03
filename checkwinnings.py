
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []  # Initialize a list to store the winning lines

    # Iterate over each line
    for line in range(lines):
        # Get the symbols in the line
        symbols_in_line = [columns[i][line] for i in range(len(columns))]

        # Check if all symbols in the line are the same and not empty
        if all(symbol != '' and symbol == symbols_in_line[0] for symbol in symbols_in_line):
            # Calculate the winnings for the line based on the symbol and bet
            line_winnings = values[symbols_in_line[0]] * bet
            winnings += line_winnings  # Accumulate total winnings
            winning_lines.append(line + 1)  # Append the line number to winning lines

    return winnings, winning_lines