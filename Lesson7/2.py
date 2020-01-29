from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def expense(self):
        return f'Расход ткани на пальто {self.name}: {(self.size / 6.5 + 0.5):.2f}'


class Suit(Clothes):
    def __init__(self, name, growth):
        self.name = name
        self.growth = growth

    @property
    def expense(self):
        return f'Расход ткани на костюм {self.name}: {(2 * self.growth + 0.3):.2f}'


a = Coat('Lacoste LX469', 200)
print(a.expense)
b = Suit('Gucci Suit X', 300)
print(b.expense)
