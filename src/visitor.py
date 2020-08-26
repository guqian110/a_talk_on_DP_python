"""Visitor pattern."""

__version__ = 1.0
__date__ = "2020-08-26"


from abc import ABCMeta, abstractmethod


class Action(metaclass=ABCMeta):
    """Vitural base class of action."""

    @abstractmethod
    def get_man_conclusion(self, man):
        """Get man conclusion."""
        pass

    @abstractmethod
    def get_woman_conclusion(self, woman):
        """Get woman conclusion."""
        pass


class Success(Action):
    """Success class."""

    def get_man_conclusion(self, man):
        """Get man conclusion."""
        print('man success')

    def get_woman_conclusion(self, woman):
        """Get woman conclusion."""
        print('woman success')


class Failure(Action):
    """Success class."""

    def get_man_conclusion(self, man):
        """Get man conclusion."""
        print('man failure')

    def get_woman_conclusion(self, woman):
        """Get woman conclusion."""
        print('woman failure')


class Person(metaclass=ABCMeta):
    """Vitural base class of person."""

    @abstractmethod
    def accept(self, action):
        """Accept visitor."""
        pass


class Man(Person):
    """Man class."""

    def accept(self, action):
        """Accept visitor."""
        action.get_man_conclusion(self)


class Woman(Person):
    """Woman class."""

    def accept(self, action):
        """Accept visitor."""
        action.get_woman_conclusion(self)


if __name__ == '__main__':
    man = Man()
    woman = Woman()
    man.accept(Success())
    woman.accept(Success())
