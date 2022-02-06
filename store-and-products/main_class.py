from modules.Product import Product
from modules.Store import Store


juice = Product("juice", 4, "drink")
milk = Product("milk", 3, "drink")

eggs = Product("eggs", 3, "food")
cereal = Product("cereal", 50, "food")

store = Store("Walmart")

store.add_product(eggs)
store.add_product(cereal)
store.add_product(juice)
store.add_product(milk)

store.display_items()

store.inflation(3)

store.display_items()

store.sell_product(3)

store.display_items()