from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, other: BankAccount, amount: float) -> bool:
        if self.withdraw(amount):
            other.deposit(amount)
            return True
        else:
            print('Insufficient funds to transfer')
            return False
