from services.auth_service import AuthService
from utils.input_validator import InputValidator
from utils.menu_display import MenuDisplay

def handle_login(auth_service: AuthService, accounts, validator: InputValidator, menu_display: MenuDisplay):
    account_number = input("Enter account number (8 digits): ")
    if not validator.validate_account_number(account_number):
        menu_display.show_error("Invalid account number format!")
        return False

    pin = input("Enter PIN (4 digits): ")
    if not validator.validate_pin(pin):
        menu_display.show_error("Invalid PIN format!")
        return False

    if auth_service.login(accounts, account_number, pin):
        menu_display.show_success("Login successful!")
        return True
    else:
        menu_display.show_error("Invalid account number or PIN!")
        return False