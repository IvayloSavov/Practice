class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.__class__.id
        self.__class__.id += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.id
