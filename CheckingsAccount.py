from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number)
        self.transfer_limit = transfer_limit

    def transfer(self, other: BankAccount, amount: float) -> bool:
        if amount <= self.transfer_limit:
            if self.withdraw(amount):
                other.deposit(amount)
                return True
            else:
                print('Insufficient funds to transfer')
                return False
        else:
            print(f'Transfer limit (${self.transfer_limit:.2f}) exceeded. Transaction failed')
            return False
