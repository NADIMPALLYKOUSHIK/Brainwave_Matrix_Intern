from .config import (
    MIN_DEPOSIT_AMOUNT,
    MAX_WITHDRAWAL_AMOUNT,
    ACCOUNT_NUMBER_LENGTH,
    PIN_LENGTH
)

class InputValidator:
    @staticmethod
    def validate_amount(amount_str, transaction_type="deposit"):
        try:
            amount = float(amount_str)
            if transaction_type == "deposit":
                return amount >= MIN_DEPOSIT_AMOUNT
            else:  # withdrawal
                return MIN_DEPOSIT_AMOUNT <= amount <= MAX_WITHDRAWAL_AMOUNT
        except ValueError:
            return False

    @staticmethod
    def validate_pin(pin_str):
        return len(pin_str) == PIN_LENGTH and pin_str.isdigit()

    @staticmethod
    def validate_account_number(acc_num):
        return len(acc_num) == ACCOUNT_NUMBER_LENGTH and acc_num.isdigit()