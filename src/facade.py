"""Facade pattern."""

__version__ = 1.0
__date__ = "2020-08-05"


class Stock1(object):
    """Stock 1."""

    def buy(self):
        """Buy in."""
        print('Buy stock 1.')

    def sell(self):
        """Sell out."""
        print('Sell stock 1.')


class Stock2(object):
    """Stock 2."""

    def buy(self):
        """Buy in."""
        print('Buy stock 2.')

    def sell(self):
        """Sell out."""
        print('Sell stock 2.')


class Stock3(object):
    """Stock 3."""

    def buy(self):
        """Buy in."""
        print('Buy stock 3.')

    def sell(self):
        """Sell out."""
        print('Sell stock 3.')


class Stock4(object):
    """Stock 4."""

    def buy(self):
        """Buy in."""
        print('Buy stock 4.')

    def sell(self):
        """Sell out."""
        print('Sell stock 4.')


class Fund(object):
    """Fund class to facade all stocks."""

    def __init__(self):
        """Fund has 4 stocks."""
        super(Fund, self).__init__()
        self._stock1 = Stock1()
        self._stock2 = Stock2()
        self._stock3 = Stock3()
        self._stock4 = Stock4()

    def buy(self):
        """Buy in fund."""
        self._stock1.buy()
        self._stock2.buy()
        self._stock3.buy()
        self._stock4.buy()

    def sell(self):
        """Sell out fund."""
        self._stock1.sell()
        self._stock2.sell()
        self._stock3.sell()
        self._stock4.sell()


if __name__ == '__main__':
    fund = Fund()
    fund.buy()
    fund.sell()
