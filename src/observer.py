"""Observer pattern."""

__version__ = 1.0
__date__ = "2020-08-07"


from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """Vitural base class of observer."""

    def __init__(self, name, subject):
        """Initilize name and subject."""
        super(Observer, self).__init__()
        self._name = name
        self._subject = subject

    @abstractmethod
    def update():
        """Update self status."""
        pass


class NBAObserver(Observer):
    """NBA observer."""

    def update(self):
        """Update self status."""
        print(self._subject.status, self._name, 'close NBA.')


class StockObserver(Observer):
    """Stock observer."""

    def update(self):
        """Update self status."""
        print(self._subject.status, self._name, 'close stock.')


class Subject(metaclass=ABCMeta):
    """Vitural base class of subject."""

    def __init__(self, name):
        """Initilize observers and status."""
        super(Subject, self).__init__()
        self._name = name
        self.status = ''
        self._observers = []

    def attach(self, observer):
        """Attach new observer."""
        self._observers.append(observer)

    def detach(self, observer):
        """Detach observer."""
        self._observers.remove(observer)

    def notify(self):
        """Notify observers to update."""
        for observer in self._observers:
            observer.update()


class Boss(Subject):
    """Boss class."""

    pass


class Secretary(Subject):
    """Secretary class."""

    pass


if __name__ == '__main__':
    # boss
    boss = Boss('Tom')
    peter = NBAObserver('Peter', boss)
    amy = StockObserver('Amy', boss)
    jack = StockObserver('Jack', boss)
    boss.attach(peter)
    boss.attach(amy)
    boss.attach(jack)
    boss.detach(jack)
    boss.status = "Boss is back."
    boss.notify()
