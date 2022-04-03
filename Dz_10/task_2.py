from abc import ABC, abstractmethod


class Closes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Closes):
    def __init__(self, name: str, v: float):
        self.name = name
        self._v = v

    @property
    def a_coat(self):
        return self._v

    def fabric_consumption(self):
        return self.a_coat / 6.5 + 0.5


class Suit(Closes):
    def __init__(self, name, h):
        self.name = name
        self._h = h

    @property
    def a_suit(self):
        return self._h

    def fabric_consumption(self):
        return 2 * self.a_suit + 0.3


class All_length:
    _length: float = 0

    @property
    def length(self):
        return self._length

    def __iadd__(self, other):
        self._length = self.length + other.fabric_consumption()
        return self


if __name__ == '__main__':
    res = All_length()
    res += Coat('Prada', 50)
    res += Suit('Dior', 150)
    print(res.length)
