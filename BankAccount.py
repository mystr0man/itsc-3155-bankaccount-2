class BankAccount:
    bank_title = "Truist"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = account_number
        self._routing_number = routing_number


    def deposit(self, dep) -> bool:
        if dep >= 0:
            self.current_balance += dep
            return True
        return False

    def withdraw(self, wd) -> bool:
            if self.current_balance - wd < self.minimum_balance:
                print("Error withdrawing $" + str(wd) + " from an account with $" + str(self.current_balance) + ": remaining balance would be below minimum balance!")
                return False
            else:
                self.current_balance -= wd
                return True

    def print_customer_information(self) -> None:
        print("At " + self.bank_title + ", " + self.customer_name + " has a balance of " + str(self.current_balance) +
              ", and their account has a minimum balance of " + str(self.minimum_balance));




Jane = BankAccount("Jane Doe", 4000, 500)
Jane.print_customer_information()
Jane.withdraw(3000)
Jane.print_customer_information()
Jane.withdraw(600)

Dickie = BankAccount("Dick Nixon", 0, 0)
Dickie.print_customer_information()
Dickie.deposit(10000000000000000000000000000000)
Dickie.print_customer_information()
