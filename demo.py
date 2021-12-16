class A:
    def __init__(self, test):
        self.test = test

    def add(self, number: int):
        self.test += number


print(A.__dict__)
