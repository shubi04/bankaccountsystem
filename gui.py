import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, holder_name, initial_balance)
            return True
        return False

    def get_account(self, account_number):
        return self.accounts.get(account_number)

class BankingGUI:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Banking Management System")
        self.root.geometry("400x300")

        # Labels and Entries
        tk.Label(root, text="Account Number:").pack(pady=5)
        self.acc_num_entry = tk.Entry(root)
        self.acc_num_entry.pack(pady=5)

        tk.Label(root, text="Holder Name:").pack(pady=5)
        self.holder_entry = tk.Entry(root)
        self.holder_entry.pack(pady=5)

        tk.Label(root, text="Amount:").pack(pady=5)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Create Account", command=self.create_account).pack(pady=5)
        tk.Button(root, text="Deposit", command=self.deposit).pack(pady=5)
        tk.Button(root, text="Withdraw", command=self.withdraw).pack(pady=5)
        tk.Button(root, text="Check Balance", command=self.check_balance).pack(pady=5)

    def create_account(self):
        acc_num = self.acc_num_entry.get()
        holder = self.holder_entry.get()
        amount = float(self.amount_entry.get() or 0)
        if self.bank.create_account(acc_num, holder, amount):
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showerror("Error", "Account number already exists.")

    def deposit(self):
        acc_num = self.acc_num_entry.get()
        amount = float(self.amount_entry.get())
        account = self.bank.get_account(acc_num)
        if account and account.deposit(amount):
            messagebox.showinfo("Success", f"Deposited ${amount}. New balance: ${account.get_balance()}")
        else:
            messagebox.showerror("Error", "Invalid account or amount.")

    def withdraw(self):
        acc_num = self.acc_num_entry.get()
        amount = float(self.amount_entry.get())
        account = self.bank.get_account(acc_num)
        if account and account.withdraw(amount):
            messagebox.showinfo("Success", f"Withdrew ${amount}. New balance: ${account.get_balance()}")
        else:
            messagebox.showerror("Error", "Invalid account or insufficient funds.")

    def check_balance(self):
        acc_num = self.acc_num_entry.get()
        account = self.bank.get_account(acc_num)
        if account:
            messagebox.showinfo("Balance", f"Balance: ${account.get_balance()}")
        else:
            messagebox.showerror("Error", "Account not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingGUI(root)
    root.mainloop()

