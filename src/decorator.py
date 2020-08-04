"""Decorator pattern."""

__version__ = 1.0
__date__ = "2020-08-04"


class Person(object):
    """Base class to be decorated."""

    def __init__(self, name):
        """Initilize person name."""
        self._name = name

    def show(self):
        """Show dress."""
        print('dressed', self._name)


class Finery(Person):
    """Virtual decorator class."""

    def __init__(self, person):
        """Component relation."""
        self._person = person

    def show(self, cash):
        """Show dress."""
        self._person.show()


class TShirts(Finery):
    """TShifts dress."""

    def show(self):
        """Show T-shirts."""
        print("T-shirts, ", end='')
        self._person.show()


class Tile(Finery):
    """Tile dress."""

    def show(self):
        """Show tile."""
        print("Tile, ", end='')
        self._person.show()


class Shoes(Finery):
    """Shoes dress."""

    def show(self):
        """Show shoes."""
        print("Shoes, ", end='')
        self._person.show()


if __name__ == '__main__':
    # Tom
    Tom = Person('Tom')
    tile = Tile(Tom)
    shoes = Shoes(tile)
    tshirts = TShirts(shoes)
    tshirts.show()
    # Peter
    Peter = Person('Perter')
    shoes = Shoes(Peter)
    tile = Tile(shoes)
    tile.show()
