from project.product import Product


class Beverage(Product):
    __name: str
    __price: float
    __milliliters: float

    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters