"""Iterator pattern."""

__version__ = 1.0
__date__ = "2020-08-20"


from abc import ABCMeta, abstractmethod


class Aggregate(metaclass=ABCMeta):
    """Vitural base class of aggregate."""

    @abstractmethod
    def create_iterator(self):
        """Create iterator."""
        pass


class MyList(Aggregate):
    """My custom list."""

    def __init__(self):
        """Initilize empty list."""
        super(MyList, self).__init__()
        self._items = []

    def create_iterator(self):
        """Create iterator."""
        return MyIterator(self)

    def count(self):
        """Count the number of items."""
        return len(self._items)

    def __setitem__(self, index, value):
        """Set value in index position."""
        if index >= len(self._items):
            self._items.append(value)
        else:
            self._items[index] = value

    def __getitem__(self, index):
        """Get the value in position."""
        return self._items[index]


class Iterator(metaclass=ABCMeta):
    """Vitural base class of iterator."""

    @abstractmethod
    def first_item(self):
        """Get first."""
        pass

    @abstractmethod
    def next_item(self):
        """Get next."""
        pass

    @abstractmethod
    def is_done(self):
        """Iterate to the last."""
        pass

    @abstractmethod
    def curr_item(self):
        """Get current item."""
        pass


class MyIterator(Iterator):
    """Iterator for MyList."""

    def __init__(self, aggregate):
        """Initilize department name."""
        super(MyIterator, self).__init__()
        self._aggregate = aggregate
        self._curr_index = 0

    def first_item(self):
        """Get first."""
        return self._aggregate[0]

    def next_item(self):
        """Get next."""
        self._curr_index += 1
        value = None
        if self._curr_index < self._aggregate.count():
            value = self._aggregate[self._curr_index]
        return value

    def is_done(self):
        """Iterate to the last."""
        return self._curr_index >= self._aggregate.count()-1

    def curr_item(self):
        """Get current item."""
        return self._aggregate[self._curr_index]


if __name__ == '__main__':
    my_list = MyList()
    my_list[0] = 'a'
    my_list[1] = 'b'
    my_list[2] = 'c'
    my_list[3] = 'd'
    my_list[4] = 'e'
    my_iterator = MyIterator(my_list)
    print('First item:', my_iterator.first_item())
    while not my_iterator.is_done():
        print('Next item:', my_iterator.next_item())
