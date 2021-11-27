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
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

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
        output = f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        output += f"----- {len(lions)} Lions:\n" + "\n".join(repr(l) for l in lions)
        output += f"\n----- {len(tigers)} Tigers:\n" + "\n".join(repr(t) for t in tigers)
        output += f"\n----- {len(cheetahs)} Cheetahs:\n" + "\n".join(repr(c) for c in cheetahs)

        return output

    def workers_status(self):
        output = f"You have {len(self.workers)} workers\n"
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]

        output += f"----- {len(keepers)} Keepers:\n" + "\n".join(repr(k) for k in keepers)
        output += f"\n----- {len(caretakers)} Caretakers:\n" + "\n".join(repr(c) for c in caretakers)
        output += f"\n----- {len(vets)} Vets:\n" + "\n".join(repr(v) for v in vets)

        return output


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
