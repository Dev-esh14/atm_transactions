"""
Create a python class ATM which has a parametrised constructor (card_no, acc_balance).
Create methods withdraw(amount) which should check if the amount is available on the
account if yes, then deduct the amount and print the message “Amount withdrawn”, if the
amount is not available then print the message “OOPS! Unable to withdraw amount, Low
balance”. Create another method called, deposit, which should deposit amount if amount is
positive and should print message “Amount deposited”. If not, print message “Invalid amount
to deposit”. Create a method called getBalance which should print current balances at any
given point of time.
Example: atm_acc_1 = ATM(“1234”, 400)
	 	 	 atm_acc_2 = ATM(“10001”, 100)
               
"""

class ATM:
    def __init__(self,card_no,acc_balance):
        self.card_no = card_no
        self.acc_balance = acc_balance
    def withdraw(self,amount):
        if(self.acc_balance>=amount):
            self.acc_balance-=amount
            print("Amount withdrawn")
        else:
            print("OOPS!Unable to withdraw amount,Low balance")
    def deposit(self,amount):
        if(amount>0):
            self.acc_balance+=amount
            print("Amount deposited")
        else:
            print("Invalid amount to deposit")
    def getBalance(self):
        print(self.acc_balance)                        

atm_acc_1=ATM("1234",400)
atm_acc_2=ATM("10001",100)
atm_acc_1.withdraw(300)
atm_acc_1.withdraw(300)
atm_acc_1.deposit(300)
atm_acc_1.getBalance()
atm_acc_2.getBalance()
atm_acc_2.deposit(300)
atm_acc_2.getBalance()


"""
OUTPUT:
Amount withdrawn
OOPS!Unable to withdraw amount,Low balance
Amount deposited
400
100
Amount deposited
400
"""
