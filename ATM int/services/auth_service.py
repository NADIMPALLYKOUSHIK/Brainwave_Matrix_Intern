class AuthService:
    def __init__(self):
        self.current_account = None

    def login(self, accounts, account_number, pin):
        for account in accounts:
            if account.account_number == account_number and account.pin == pin:
                self.current_account = account
                return True
        return False

    def logout(self):
        self.current_account = None

    def get_current_account(self):
        return self.current_account