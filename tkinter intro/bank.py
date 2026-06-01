import tkinter as tk


class BankAccount:
    
    def __init__(self, account):
        self.account = account
        self.balance = 0 
        pass


    def deposit(self, amount):
        self.balance += amount
        pass
    def withdraw(self, amount):
        self.balance -= amount
        pass


class BankGUI:
    def __init__(self, root):
        self.root = root
        self.account = None
        self.root.title("Bank Account")
        self.root.geometry("500x500")

        self.create_frames()
        self.create_widgets()
        pass

    def create_frames(self):
        self.input_frame = tk.Frame(self.root, padx=10, pady=10)
        self.display_frame = tk.Frame(self.root, padx=10, pady=10)
        self.button_frame = tk.Frame(self.root, padx=10, pady=10)

        self.input_frame.pack(fill="x")
        self.display_frame.pack(fill="x")
        self.button_frame.pack(fill="x")

        pass

    def create_widgets(self):
        tk.Label(self.input_frame, text="Account Name:").grid(row=0, column=0)

        self.account_entry = tk.Entry(self.input_frame)
        self.account_entry.grid(row=0, column=1)

        tk.Button(
            self.input_frame,
            text="Create Account",
            command=self.create_account
        ).grid(row=0, column=2)


        self.account_label = tk.Label(self.display_frame, text="Welcome : ")
        self.account_label.pack()

        self.balance_label = tk.Label(self.display_frame, text="Balance : $")
        self.balance_label.pack()

        tk.Label(self.button_frame, text="Transaction Amount: $").grid(row=0, column=0)
        self.amount_entry = tk.Entry(self.button_frame)
        self.amount_entry.grid(row=0, column=1)

        tk.Button(self.button_frame, text="Deposit", width=15, 
                  command=self.deposit_amount).grid(row=1, column=0, pady=5)
        
        tk.Button(self.button_frame, text="Withdraw", width=15, 
                  command=self.withdraw_amount).grid(row=1, column=1, pady=5)

    def create_account(self):
        account_input = self.account_entry.get().strip()
        if account_input != "":
            self.account = BankAccount(account_input)
            self.update_display()

    def update_display(self):
        if self.account is not None:
            self.account_label.config(text=f"Welcome : {self.account.account}")
            self.balance_label.config(text=f"Balance : ${self.account.balance}")

    def deposit_amount(self):
        if self.account is not None:
            amount = float(self.amount_entry.get())
            self.account.deposit(amount)
            self.update_display()
        pass
    def withdraw_amount(self):
        if self.account is not None:
            amount = float(self.amount_entry.get())
            self.account.withdraw(amount)
            self.update_display()
        pass
        
if __name__ == "__main__":

    root = tk.Tk()
    root.title("Bank Account")
    app = BankGUI(root)
    root.mainloop()

    
    