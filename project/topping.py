class Topping:
    topping_type: str
    weight: float

    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    