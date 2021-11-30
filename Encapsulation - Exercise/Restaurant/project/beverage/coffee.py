from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    __name: str
    __price: float
    __milliliters: float
    __caffeine: float
    MILLILITERS: int = 50
    PRICE: float = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
