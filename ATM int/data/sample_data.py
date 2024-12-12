from models.account import Account

def get_sample_accounts():
    return [
        Account("12345678", "1234", 1000.0),
        Account("87654321", "4321", 2000.0)
    ]