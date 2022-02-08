from Modules.Animal import Animal


class Penguin(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age, health=30, happiness=65)

    def walk(self):
        print(f"{self.name} waddles around")

    def feed(self):
        self.happiness += 15
        self.health += 15