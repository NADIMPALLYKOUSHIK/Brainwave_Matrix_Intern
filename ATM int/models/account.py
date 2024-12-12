from .transaction import Transaction

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(Transaction("Deposit", amount))
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(Transaction("Withdrawal", amount))
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return [str(transaction) for transaction in self.transaction_history]