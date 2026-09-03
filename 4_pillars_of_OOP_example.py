class BankAccount:
    def __init__(self,__accno,__bal=0):
        self.__accno = __accno    #private attribues
        self.__bal = __bal


    def check_bal(self,amount=0):
        self.__bal = amount
        print(self.__bal)


    def deposite(self,amount):
        self.__bal+=amount
        print(f"You have deposited {amount}.")
        print("Bank balance is",self.__bal)
        print()


    def withdraw(self,amount):

        if self.__bal<amount:
            print(f"You cannot withdraw {amount}.")
            print("Bank balance is only",self.__bal)
            print()
            
        else:
            self.__bal -= amount
            print(f"You withdraw successfully {amount}.")
            print("Bank balance is",self.__bal)
            print()


acc1=BankAccount(123,10000)
acc1.deposite(20000)
acc1.withdraw(1000)
