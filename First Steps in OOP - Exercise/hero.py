class Hero:
    name: str
    health: int

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        if self.health - damage <= 0:
            self.health = 0
            return f"{self.name} was defeated"

        self.health -= damage

    def heal(self, amount: int):
        self.health += amount

