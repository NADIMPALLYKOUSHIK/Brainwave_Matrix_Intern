class MenuDisplay:
    @staticmethod
    def show_welcome():
        print("\n" + "="*30)
        print("Welcome to the ATM System")
        print("="*30)

    @staticmethod
    def show_main_menu():
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Logout")
        print("="*15)

    @staticmethod
    def show_balance(balance):
        print(f"\nCurrent balance: ${balance:.2f}")
        print("-"*30)

    @staticmethod
    def show_transaction_history(transactions):
        if not transactions:
            print("\nNo transactions to display")
            return
            
        print("\nTransaction History:")
        print("-"*30)
        for transaction in transactions:
            print(transaction)
        print("-"*30)

    @staticmethod
    def show_error(message):
        print(f"\n❌ Error: {message}")

    @staticmethod
    def show_success(message):
        print(f"\n✅ Success: {message}")