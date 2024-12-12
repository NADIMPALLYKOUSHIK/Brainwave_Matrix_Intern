from utils.input_validator import InputValidator
from utils.menu_display import MenuDisplay
from services.atm_service import ATMService

def handle_balance(atm_service: ATMService, current_account, menu_display: MenuDisplay):
    try:
        balance = atm_service.check_balance(current_account)
        menu_display.show_balance(balance)
    except Exception as e:
        menu_display.show_error(f"Error checking balance: {str(e)}")

def handle_deposit(atm_service: ATMService, current_account, validator: InputValidator, menu_display: MenuDisplay):
    amount = input("Enter amount to deposit: $")
    if not validator.validate_amount(amount, "deposit"):
        menu_display.show_error("Invalid amount! Amount must be positive.")
        return
    
    try:
        if atm_service.deposit(current_account, float(amount)):
            menu_display.show_success(f"Successfully deposited ${float(amount):.2f}")
        else:
            menu_display.show_error("Deposit failed")
    except Exception as e:
        menu_display.show_error(f"Error processing deposit: {str(e)}")

def handle_withdrawal(atm_service: ATMService, current_account, validator: InputValidator, menu_display: MenuDisplay):
    amount = input("Enter amount to withdraw: $")
    if not validator.validate_amount(amount, "withdrawal"):
        menu_display.show_error("Invalid amount! Please check withdrawal limits.")
        return
    
    try:
        if atm_service.withdraw(current_account, float(amount)):
            menu_display.show_success(f"Successfully withdrew ${float(amount):.2f}")
        else:
            menu_display.show_error("Insufficient funds or invalid amount")
    except Exception as e:
        menu_display.show_error(f"Error processing withdrawal: {str(e)}")