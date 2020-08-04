"""Proxy pattern."""

__version__ = 1.0
__date__ = "2020-08-04"


from abc import ABCMeta, abstractmethod


class IGiveGift(metaclass=ABCMeta):
    """Vitural base interface class to give gifts."""

    @abstractmethod
    def give_dolls(self):
        """Give dolls."""
        pass

    @abstractmethod
    def give_flowers(self):
        """Give flowers."""
        pass

    @abstractmethod
    def give_chocolate(self):
        """Give chocolate."""
        pass


class Pursuit(IGiveGift):
    """Subject class to be proxyed."""

    def __init__(self, girl):
        """Refer to girl."""
        self._girl = girl

    def give_dolls(self):
        """Give dolls."""
        print('Give', self._girl._name, 'dolls.')

    def give_flowers(self):
        """Give flowers."""
        print('Give', self._girl._name, 'flowers.')

    def give_chocolate(self):
        """Give chocolate."""
        print('Give', self._girl._name, 'chocolate.')


class Proxy(IGiveGift):
    """Proxy of Pursuit class."""

    def __init__(self, girl):
        """Refer to pursuit."""
        super(Proxy, self).__init__()
        self._pursuit = Pursuit(girl)

    def give_dolls(self):
        """Give dolls."""
        self._pursuit.give_dolls()

    def give_flowers(self):
        """Give flowers."""
        self._pursuit.give_flowers()

    def give_chocolate(self):
        """Give chocolate."""
        self._pursuit.give_chocolate()


class SchoolGirl(object):
    """SchoolGirl class."""

    def __init__(self, name):
        """Initilize girl's name."""
        super(SchoolGirl, self).__init__()
        self._name = name


if __name__ == '__main__':
    girl = SchoolGirl('JiaoJiao')
    proxy = Proxy(girl)
    proxy.give_dolls()
    proxy.give_flowers()
    proxy.give_chocolate()
