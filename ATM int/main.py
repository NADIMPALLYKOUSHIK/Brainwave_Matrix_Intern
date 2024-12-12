from models.account import Account
from services.auth_service import AuthService
from services.atm_service import ATMService
from utils.input_validator import InputValidator
from utils.menu_display import MenuDisplay
from utils.menu_handler import MenuHandler
from handlers.auth_handlers import handle_login
from handlers.transaction_handlers import handle_balance, handle_deposit, handle_withdrawal
from data.sample_data import get_sample_accounts

def main():
    # Initialize services and utilities
    accounts = get_sample_accounts()
    auth_service = AuthService()
    atm_service = ATMService()
    validator = InputValidator()
    menu_display = MenuDisplay()
    menu_handler = MenuHandler()

    def setup_menu_actions():
        current_account = auth_service.get_current_account()
        
        menu_handler.register_action("1", 
            lambda: handle_balance(atm_service, current_account, menu_display))
        menu_handler.register_action("2", 
            lambda: handle_deposit(atm_service, current_account, validator, menu_display))
        menu_handler.register_action("3", 
            lambda: handle_withdrawal(atm_service, current_account, validator, menu_display))
        menu_handler.register_action("4", 
            lambda: menu_display.show_transaction_history(atm_service.view_history(current_account)))
        menu_handler.register_action("5", 
            lambda: [auth_service.logout(), menu_display.show_success("Logged out successfully!")])

    while True:
        if auth_service.get_current_account() is None:
            menu_display.show_welcome()
            if not handle_login(auth_service, accounts, validator, menu_display):
                continue
            setup_menu_actions()

        menu_display.show_main_menu()
        choice = input("Enter your choice (1-5): ")

        if not menu_handler.handle_choice(choice):
            menu_display.show_error("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

    