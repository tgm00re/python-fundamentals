class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        self.products.pop(id)

    def inflation(self, percent_increase):
        for prod in self.products:
            prod.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for prod in self.products:
            if(prod.category == category):
                prod.update_price(percent_discount, False)

    def display_items(self):
        for prod in self.products:
            prod.print_info()

    