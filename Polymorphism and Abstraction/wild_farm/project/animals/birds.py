from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        if isinstance(food, Food):
            self.weight += food.quantity * 0.35
            self.food_eaten += food.quantity
