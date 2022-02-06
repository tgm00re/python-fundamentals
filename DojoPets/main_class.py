from modules.pet import Dog, Cat
from modules.ninja import Ninja


rufus = Dog("Rufus", "Dog", ["Roll Over", "Play Dead"], 50, 25)
ninjaMan = Ninja("Ninja", "Man", rufus, "Cookies", "Kibble")

rufus.noise()

ninjaMan.bathe()

fleabag = Cat("Flebag", "Cat", ["Scream", "Scratch People"], 10, 10)
kristin = Ninja("Kristin", "M", fleabag, "plants", "blood")

kristin.bathe()
kristin.feed()
kristin.walk()

