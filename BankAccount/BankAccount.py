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

    def getBalance(self):
        return self.balance
        
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def displayAccountsInfo(cls):
        for acc in cls.accounts:
            print(acc.balance)

    @staticmethod
    def hasEnough(amount, balance):
        if(amount <= balance):
            return True
        return False



class User:
    def __init__(self):
        self.savings = BankAccount(.05, 500)
        self.spendings = BankAccount(.01, 250)

    def deposit(self, amount, accountType):
        if(accountType == "spendings"):
            self.spendings.deposit(amount)
        elif(accountType == "savings"):
            self.savings.deposit(amount)
        return self

    def withdraw(self, amount, accountType):
        if(accountType == "spendings"):
            self.spendings.withdraw(amount)
        elif(accountType == "savings"):
            self.savings.withdraw(amount)
        return self

    def display_balance(self, accountType):
        if(accountType == "spendings"):
            self.spendings.display_account_info()
        elif(accountType == "savings"):
            self.savings.display_account_info()
        return self

    def transfer_balance(self, user, amount, accountType, accountType2):
        if(accountType == "spendings"):
            if(self.spendings.hasEnough(amount, self.spendings.getBalance())):
                self.spendings.withdraw(amount)
                if(accountType2 == "spendings"):
                    user.spendings.deposit(amount)
                elif(accountType2 == "savings"):
                    user.savings.deposit(amount)
            else:
                print("sorry, not enough money :(")
        elif(accountType == "savings"):
            if(self.savings.hasEnough(amount, self.savings.getBalance())):
                self.savings.withdraw(amount)
                if(accountType2 == "spendings"):
                    user.spendings.deposit(amount)
                elif(accountType2 == "savings"):
                    user.savings.deposit(amount)
            else:
                print("sorry, not enough money :(")
        
        return self

user1 = User()
user2 = User()

user1.deposit(500, "spendings")
user1.display_balance("spendings")
user1.display_balance("savings")

user2.transfer_balance(user2, 100, "spendings", "savings")
user2.display_balance("savings")