from Modules.Animal import Animal


class Giraffe(Animal):
    def __init__(self, name, age, height):
        super().__init__(name, age, health=45, happiness=75)
        self.height = height

    def lick(self):
        print(f"{self.name} licks the most nearby humanoid")
    
    def feed(self):
        self.health += 45