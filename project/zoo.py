from typing import Union, List
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker
from project.animal import Animal


class Zoo:
    name: str
    __budget: int
    __animal_capacity: int
    __workers_capacity: int
    animals: List[Union[Lion, Tiger, Cheetah]]
    workers: List[Union[Keeper, Caretaker, Vet]]

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Union[Tiger, Cheetah, Lion, Animal], price) -> str:
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Union[Vet, Keeper, Caretaker, Worker]) -> str:
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} added to the zoo"

    def fire_worker(self, worker_name) -> str:
        worker_names = [w.name for w in self.workers]

        if worker_name not in worker_names:
            return f"There is no {worker_name} in the zoo"

        self.workers.pop(worker_names.index(worker_name))
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        needed_money = sum([w.salary for w in self.workers])
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        needed_money = sum([a.money_for_care for a in self.animals])
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):
        pass

    def workers_status(self):
        pass