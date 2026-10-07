from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def attack(self):
        print(f"{self.name} рубит мечом на {self.damage} урона")

class Mage(Hero):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def attack(self):
        print(f"{self.name} пускает огненный шар на {self.damage} урона")

heroes = [
    Warrior("Arthor", 50),
    Mage("Killian", 70)
]

for hero in heroes:
    hero.attack()
