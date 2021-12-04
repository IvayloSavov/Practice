from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_con_per_kilometer = 0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.air_con_per_kilometer)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed


class Truck(Vehicle):
    air_con_per_kilometer = 1.6

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.air_con_per_kilometer)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

