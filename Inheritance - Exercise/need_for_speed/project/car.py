from project import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION: float = 3.00

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

