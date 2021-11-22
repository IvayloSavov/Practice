class Vet:
    animals: list = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, name):
        if len(Vet.animals) == Vet.space:
            return "Not enough space"

        self.animals.append(name)
        Vet.animals.append(name)

        return f"{name} registered in the clinic"

    def unregister_animal(self, name):
        if name in self.animals:
            self.animals.remove(name)
            Vet.animals.remove(name)
            return f"{name} unregistered successfully"
        return f"{name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(self.animals)} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
