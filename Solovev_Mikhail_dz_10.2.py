from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):

    @property
    def calc(self):
        return round((self.size / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calc(self):
        return round((2 * self.size) + 0.3)


a = Coat(50)
print(a.calc)
b = Suit(180)
print(b.calc)
