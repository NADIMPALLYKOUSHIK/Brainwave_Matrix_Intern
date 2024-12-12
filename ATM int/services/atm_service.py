class ATMService:
    @staticmethod
    def deposit(account, amount):
        return account.deposit(amount)

    @staticmethod
    def withdraw(account, amount):
        return account.withdraw(amount)

    @staticmethod
    def check_balance(account):
        return account.get_balance()

    @staticmethod
    def view_history(account):
        return account.get_transaction_history()