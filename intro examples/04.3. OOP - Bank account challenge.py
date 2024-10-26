
class Account():
    
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amount):
        self.balance += dep_amount
        print("Deposit accepted. New balance: " + str(self.balance))


    def withdraw(self, witd_amount):
        if self.balance >= witd_amount:
            self.balance -= witd_amount
            print("Withdrawal accepted. New balance: " + str(self.balance))
        else:
            print("Insufficient funds.")

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'


acct1 = Account('Jose',100)
print(acct1)

acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
