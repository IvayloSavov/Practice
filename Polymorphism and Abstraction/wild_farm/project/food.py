from abc import ABC


class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food):
    pass



