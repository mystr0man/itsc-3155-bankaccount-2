class BankAccount:
    bank_title = "Truist"
    _routing_number = "1"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = account_number


    def deposit(self, dep) -> bool:
        if dep >= 0:
            self.current_balance += dep
            return True
        return False

    def withdraw(self, wd) -> bool:
            if self.current_balance - wd < self.minimum_balance:
                print(f"Error withdrawing ${wd:.2f} from an account with ${self.current_balance:.2f}: remaining balance would be below minimum balance of ${self.minimum_balance:.2f}!")
                return False
            else:
                self.current_balance -= wd
                return True

    def print_customer_information(self) -> None:
        print(f"At {self.bank_title}, {self.customer_name} has a balance of ${self.current_balance:.2f}, and their account has a minimum balance of ${self.minimum_balance:.2f}");
        print(f"They also have a routing number of {self._routing_number} and an account number of {self.__account_number}")
