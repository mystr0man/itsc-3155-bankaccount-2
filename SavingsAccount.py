from BankAccount import BankAccount


class SavingsAccount(BankAccount, interest_rate):
    def __init__(self, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.current_balance *= (1 + interest_rate)

