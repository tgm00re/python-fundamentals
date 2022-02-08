from Modules.Animal import Animal

class Tiger(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age, health=50, happiness=50)

    def feed(self):
        self.happiness += 25
        self.health += 10

