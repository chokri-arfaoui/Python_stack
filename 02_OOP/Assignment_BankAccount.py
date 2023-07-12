class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self,int_rate=0.02, balance=0 ): 
        if balance!=0:
            self.balance=balance
        else :
            balance=0
        self.int_rate= int_rate
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
        return self
    
        # your code here
    def withdraw(self, amount):
        if self.balance >=amount:
            self.balance-=amount# your code here
        else:
            print( "Insufficient funds: Charging a $5 fee")
            self.balance-= (amount+5)
        
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self
    #     # your code here
    def yield_interest(self):
        if self.balance>0:
            self.balance+=self.balance*self.int_rate
        return self
BankAccount_1=BankAccount(0.02,200)
BankAccount_2=BankAccount(0.02,300)
BankAccount_1.deposit(50).deposit(100).deposit(20).withdraw(250).yield_interest().display_account_info()
BankAccount_2.deposit(120).deposit(80).withdraw(100).withdraw(40).withdraw(60).withdraw(70).yield_interest().display_account_info()