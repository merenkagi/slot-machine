#global values are in CAPITALS, and these will for the user's input
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
       
def deposit ():                                    #this function collects user input and gets the deposit from the user
    while True:                                    #the while loop will continuously ask the user for input until we get a valid amount
        amount = input("What would you like to deposit? R")
        if amount.isdigit():                       # isdigit will tell us if this is a valid whole number
            amount = int(amount)                   # if amount is a valid number, convert this to an integer
            if amount > 0:                  
                break
            else:
                print ("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines() :
    while True:   #the while loop will continuously ask the user for input until we get a valid amount
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():                       # isdigit will tell us if this is a valid whole number
            lines = int(lines)                    # if amount is a valid number, convert this to an integer
            if 1 <= lines <= MAX_LINES:                  
                break
            else:
                print ("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
            
    return lines

def get_bet():
    while True:   #the while loop will continuously ask the user for input until we get a valid amount
        amount = input("What would you like to bet on each line? R")
        if amount.isdigit():                     # isdigit will tell us if this is a valid whole number
            amount = int(amount)                 # if amount is a valid number, convert this to an integer
            if MIN_BET <= amount <= MAX_BET:                  
                break
            else:
                print (f"Amount must be between R{MIN_BET} - R{MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount


                
 