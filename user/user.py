class User:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Sorry, not enough balance!")
        return self

    def display_balance(self):
        print("balance: " + str(self.balance))
        return self

    def transfer_balance(self, user, amount):
        if(amount <= self.balance):
            user.balance += amount
            self.balance -= amount
        else:
            print("sorry, you don't have that much!")
        return self

jerry = User()
jerry.deposit(100).display_balance().withdraw(200)

kathy = User()
kathy.deposit(500).transfer_balance(jerry, 300)
kathy.transfer_balance(jerry, 300)

jerry.display_balance()
kathy.display_balance()