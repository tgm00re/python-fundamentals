from traceback import print_exception
from unicodedata import name


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        price_change = self.price * (percent_change / 100)
        if(is_increased):
            self.price += price_change
        else:
            self.price -= price_change

    def print_info(self):
        print(f"Product name: {self.name} | Category: {self.category} | Price: {self.price}")