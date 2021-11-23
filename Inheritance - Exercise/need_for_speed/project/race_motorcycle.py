from project import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION: float = 8.00

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)