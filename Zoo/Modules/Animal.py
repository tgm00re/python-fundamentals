class Animal:
    def __init__(self, name, age, health, happiness) -> None:
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def feed(self):
        self.happiness += 10
        self.health += 10

    def display_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Health: {self.health} | Happiness: {self.happiness}")