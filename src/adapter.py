"""Adapter pattern."""

__version__ = 1.0
__date__ = "2020-08-19"


from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    """Vitural base class of player."""

    @abstractmethod
    def attack(self):
        """Attck."""
        pass

    @abstractmethod
    def defence(self):
        """Defence."""
        pass


class Forward(Player):
    """Forward player."""

    def __init__(self, name):
        """Initilize player name."""
        super(Forward, self).__init__()
        self._name = name

    def attack(self):
        """Attack of forward."""
        print("Forward", self._name, "attack.")

    def defence(self):
        """Defence of forward."""
        print("Forward", self._name, "defence.")


class Center(Player):
    """Center player."""

    def __init__(self, name):
        """Initilize player name."""
        super(Center, self).__init__()
        self._name = name

    def attack(self):
        """Attack of center."""
        print("Center", self._name, "attack.")

    def defence(self):
        """Defence of center."""
        print("Center", self._name, "defence.")


class Guard(Player):
    """Guard player."""

    def __init__(self, name):
        """Initilize player name."""
        super(Guard, self).__init__()
        self._name = name

    def attack(self):
        """Attack of guard."""
        print("Guard", self._name, "attack.")

    def defence(self):
        """Defence of guard."""
        print("Guard", self._name, "defence.")


class ForeignCenter(object):
    """Foreign center player."""

    def __init__(self, name):
        """Initilize player name."""
        super(ForeignCenter, self).__init__()
        self._name = name

    def jingong(self):
        """Attack of foreign center."""
        print("Foreign center", self._name, "attack.")

    def fangshou(self):
        """Defence of foreign center."""
        print("Foreign center", self._name, "defence.")


class Translator(Player):
    """Translator for foreign center."""

    def __init__(self, name):
        """Initilize player name."""
        super(Translator, self).__init__()
        self._foreign_center = ForeignCenter(name)

    def attack(self):
        """Translate attack to foreign center."""
        self._foreign_center.jingong()

    def defence(self):
        """Translate defence to foreign center."""
        self._foreign_center.fangshou()


if __name__ == '__main__':
    Battier = Forward('Battier')
    Battier.attack()
    McGrady = Guard('McGrady')
    McGrady.attack()
    YaoMing = Translator('YaoMing')
    YaoMing.attack()
    YaoMing.defence()
