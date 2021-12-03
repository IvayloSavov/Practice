from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + (self.__class__.air_con_per_kilometer * distance)
        

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    air_con_per_kilometer = 0.9
    pass


class Truck(Vehicle):
    air_con_per_kilometer = 1.6
    pass
