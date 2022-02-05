class BankAccount:

    accounts = []
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficnet funds: Charging a $5 fee and deduct $5")
        return self
        
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def displayAccountsInfo(cls):
        for acc in cls.accounts:
            print(acc.balance)




acc1 = BankAccount(balance=5)
acc2 = BankAccount(0.05)

acc1.deposit(20).deposit(25).deposit(25).yield_interest().display_account_info()

acc2.deposit(100).deposit(100).withdraw(10).withdraw(20).withdraw(50).withdraw(5).yield_interest().display_account_info()

BankAccount.displayAccountsInfo()

