from Modules.Giraffe import Giraffe
from Modules.Animal import Animal
from Modules.Penguin import Penguin
from Modules.Tiger import Tiger

class Zoo:
    def __init__(self, zoo_name) -> None:
        self.animals = []
        self.name = zoo_name

    def add_tiger(self, name, age):
        self.animals.append( Tiger(name, age) )

    def add_girrafe(self, name, age, height):
        self.animals.append( Giraffe(name, age, height) )

    def add_penguin(self, name, age):
        self.animals.append( Penguin(name, age) )

    def print_animals(self):
        for animal in self.animals:
            animal.display_info()

    
my_zoo = Zoo("My Zoo")
print(my_zoo.name)
my_zoo.add_girrafe("Jerry", 42, 300)
my_zoo.add_tiger("Bruce", 12)
my_zoo.add_penguin("Lemon", 3)
my_zoo.print_animals()




