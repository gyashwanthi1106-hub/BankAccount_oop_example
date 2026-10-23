class BankAccount:
    def __init__(self, accno, bal=0):
        # ENCAPSULATION: the account number and balance are private (double underscore)
        # so they can only be changed through the methods below
        self.__accno = accno
        self.__bal = bal

    def get_balance(self):
        return self.__bal

    def check_bal(self):
        # only shows the balance, it never changes it
        print("Bank balance is", self.__bal)
        print()

    # ABSTRACTION: the user just calls deposit() or withdraw() and does not
    # need to know how the balance is stored or updated inside
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be more than 0.")
            print()
            return
        self.__bal += amount
        print(f"You have deposited {amount}.")
        print("Bank balance is", self.__bal)
        print()

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be more than 0.")
            print()
        elif self.__bal < amount:
            print(f"You cannot withdraw {amount}.")
            print("Bank balance is only", self.__bal)
            print()
        else:
            self.__bal -= amount
            print(f"You withdraw successfully {amount}.")
            print("Bank balance is", self.__bal)
            print()


# INHERITANCE: SavingsAccount gets everything from BankAccount (deposit, check_bal ...)
class SavingsAccount(BankAccount):
    def __init__(self, accno, bal=0, min_balance=1000):
        super().__init__(accno, bal)
        self.min_balance = min_balance

    # POLYMORPHISM: same method name (withdraw) but a different behaviour,
    # a savings account must always keep a minimum balance
    def withdraw(self, amount):
        if self.get_balance() - amount < self.min_balance:
            print(f"You cannot withdraw {amount}.")
            print(f"A savings account must keep at least {self.min_balance}.")
            print("Bank balance is", self.get_balance())
            print()
        else:
            super().withdraw(amount)


acc1 = BankAccount(123, 10000)
acc1.deposit(20000)
acc1.withdraw(1000)
acc1.check_bal()

acc2 = SavingsAccount(456, 5000)
acc2.withdraw(4500)  # not allowed, it would go below the minimum balance
acc2.withdraw(3000)  # allowed

# the same call works for both kinds of account
for account in [acc1, acc2]:
    account.withdraw(100)
