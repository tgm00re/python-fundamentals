class User:
    balance = 0
    def __init__(self):
        pass

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Sorry, not enough balance!")

    def display_balance(self):
        print("balance: " + str(self.balance))

    def transfer_balance(self, user, amount):
        if(amount <= self.balance):
            user.balance += amount
            self.balance -= amount
        else:
            print("sorry, you don't have that much!")

jerry = User()
jerry.deposit(100)
jerry.display_balance()
jerry.withdraw(200)

kathy = User()
kathy.deposit(500)
kathy.transfer_balance(jerry, 300)

jerry.display_balance()