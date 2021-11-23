from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    customers: List[Customer]
    dvds: List[DVD]

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next(c for c in self.customers if c.id == customer_id)
        dvd = next(dvd for dvd in self.dvds if dvd.id == dvd_id)

        if dvd.is_rented:
            return "DVD is already rented"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        self.dvds.remove(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = next(c for c in self.customers if c.id == customer_id)
        dvd = next(dvd for dvd in self.dvds if dvd.id == dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        self.dvds.append(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        return "\n".join(repr(c) for c in self.customers) + "\n" + "\n".join(repr(dvd) for dvd in self.dvds) + "\n"


# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))

# print(movie_world)
