from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        self.current_balance *= (1 + self.interest_rate)

    def print_customer_information(self) -> None:
        super()
        print(f"As a savings account, their account has an interest rate of {self.interest_rate}")