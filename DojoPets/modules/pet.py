

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy += 25

    def eat(self):
        self.health += 10
        self.energy += 5

    def play(self):
        self.health += 5
    
    def noise(self):
        raise NotImplementedError



class Dog(Pet):
    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)

    def noise(self):
        print("Bork")

class Cat(Pet):
    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)

    def noise(self):
        print("Miau")
