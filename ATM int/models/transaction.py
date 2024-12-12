class Transaction:
    def __init__(self, transaction_type: str, amount: float):
        self.transaction_type = transaction_type
        self.amount = amount
        
    def __str__(self):
        symbol = "+" if self.transaction_type == "Deposit" else "-"
        return f"{self.transaction_type}: {symbol}${self.amount:.2f}"