from SavingsAccount import SavingsAccount
from CheckingsAccount import CheckingAccount

print('Jane')
Jane = CheckingAccount("Jane Doe", 4_000, 500, 100, 10_000)
Jane.print_customer_information()
Jane.withdraw(3_000)
Jane.print_customer_information()
Jane.withdraw(600)

print()
print('Dickie')
Dickie = SavingsAccount("Dick Nixon", 0, 0, 101, 0.5)
Dickie.print_customer_information()
Dickie.deposit(1_000_000)
Dickie.print_customer_information()

print()
print('Jane transfers $100 to Dickie')
Jane.transfer(Dickie, 100)
Jane.print_customer_information()
Dickie.print_customer_information()

print()
print('Jane fails to transfer $500 to Dickie')
Jane.transfer(Dickie, 500)
Jane.print_customer_information()
Dickie.print_customer_information()

print()
print('Dickie gains interest')
Dickie.print_customer_information()
for i in range(5):
    Dickie.apply_interest()
Dickie.print_customer_information()
