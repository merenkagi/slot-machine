import tkinter as tk
from tkinter import messagebox
import random

class SlotMachineApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Slot Machine")
        
        self.balance = 100  # Starting balance
        self.lines = 1      # Default number of lines
        self.bet = 1        # Default bet amount
        
        # Create widgets
        self.balance_label = tk.Label(master, text=f"Balance: ${self.balance}")
        self.lines_label = tk.Label(master, text="Lines to bet on:")
        self.lines_entry = tk.Entry(master)
        self.bet_label = tk.Label(master, text="Bet amount:")
        self.bet_entry = tk.Entry(master)
        self.spin_button = tk.Button(master, text="Spin", command=self.spin)
        
        # Layout widgets
        self.balance_label.grid(row=0, column=0)
        self.lines_label.grid(row=1, column=0)
        self.lines_entry.grid(row=1, column=1)
        self.bet_label.grid(row=2, column=0)
        self.bet_entry.grid(row=2, column=1)
        self.spin_button.grid(row=3, column=0, columnspan=2)
    
    def spin(self):
        try:
            self.lines = int(self.lines_entry.get())
            self.bet = int(self.bet_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for lines and bet.")
            return
        
        if self.bet > self.balance:
            messagebox.showerror("Error", "You do not have enough balance to place this bet.")
            return
        
        symbols = ['A', 'B', 'C', 'D']
        result = [[random.choice(symbols) for _ in range(3)] for _ in range(self.lines)]
        
        self.display_result(result)
        self.update_balance()
    
    def display_result(self, result):
        result_str = '\n'.join([' '.join(row) for row in result])
        messagebox.showinfo("Result", result_str)
    
    def update_balance(self):
        self.balance -= self.bet
        self.balance_label.config(text=f"Balance: ${self.balance}")

def main():
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()