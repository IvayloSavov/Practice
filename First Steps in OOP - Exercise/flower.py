class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, amount):
        if amount >= self.water_requirements:
            self.is_happy = True

    def status(self):
        return f"{self.name} {'is' if self.is_happy else 'is not'} happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

