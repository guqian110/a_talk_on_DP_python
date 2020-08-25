"""Mediator pattern."""

__version__ = 1.0
__date__ = "2020-08-25"


from abc import ABCMeta, abstractmethod


class Country(object):
    """Vitural base class of country."""

    def __init__(self, un):
        """Country has a mediator."""
        super(Country, self).__init__()
        self._un = un

    def declare(self, message):
        """Declare a message via the mediator."""
        self._un.declare(self, message)


class USA(Country):
    """USA country."""

    def get_message(self, message):
        """Receive message from others."""
        print('USA get message:', message)


class Iraq(Country):
    """Irqa country."""

    def get_message(self, message):
        """Receive message from others."""
        print('Iraq get message:', message)


class UnitedNations(metaclass=ABCMeta):
    """Vitural base class of the UN."""

    @abstractmethod
    def declare(self, country, message):
        """Declare a message to a country."""
        pass


class UnitedNationsSecurityCouncil(UnitedNations):
    """The SecurityCouncil of the UN."""

    def __init__(self):
        """Initialize two countries."""
        super(UnitedNationsSecurityCouncil, self).__init__()
        self.usa = None
        self.iraq = None

    def declare(self, country, message):
        """Declare a message to a country."""
        if country == usa:
            self.iraq.get_message(message)
        else:
            self.usa.get_message(message)


if __name__ == '__main__':
    unsc = UnitedNationsSecurityCouncil()
    usa = USA(unsc)
    iraq = Iraq(unsc)
    unsc.usa = usa
    unsc.iraq = iraq
    usa.declare('Stop nuclear weapons!')
    iraq.declare('No nuclear weapons!')
