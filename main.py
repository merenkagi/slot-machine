'''this commented out code is a simple terminal app for this

import random
import userinput  # Importing functions from userinput.py
import slotmachinedesign
import checkwinnings 

def main():
    balance = userinput.deposit()  # Accessing deposit function from userinput.py
    lines = userinput.get_number_of_lines()  # Accessing get_number_of_lines function from userinput.py
    while True:
        bet = userinput.get_bet()  # Accessing get_bet function from userinput.py
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting R{bet} on {lines} lines. Total is equal to: ${total_bet}")
    
    slots = slotmachinedesign.get_slot_machine_spin(slotmachinedesign.ROWS, slotmachinedesign.COLS, slotmachinedesign.symbol_count)
    slotmachinedesign.print_slot_machine(slots)  # Assuming slotmachinedesign.py contains print_slot_machine function
    
    winnings, winning_lines = checkwinnings.check_winnings(slots, lines, bet, slotmachinedesign.values)
    print(f"You won R1{winnings}.")
    print(f"You won on:", *winning_lines)       # * is the unpack operator and will pass every single line from the winning lines list to this print function
    
    
main()'''

import slot_machine_gui

def main():
    # You can add any initialization code here if needed
    slot_machine_gui.main()

if __name__ == "__main__":
    main()