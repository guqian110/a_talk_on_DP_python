"""Strategy pattern."""

__version__ = 1.0
__date__ = "2020-07-30"


from abc import ABCMeta, abstractmethod


class CashSuper(metaclass=ABCMeta):
    """Vitural base class for all cash calculations."""

    @abstractmethod
    def accept_cash(self, cash):
        """Calculate cashes."""
        pass


class CashNormal(CashSuper):
    """Normal calculation."""

    def accept_cash(self, cash):
        """No calculation."""
        return cash


class CashRebate(CashSuper):
    """Discount calculation."""

    def __init__(self, rebate):
        """Initilize rebate."""
        self.rebate = rebate

    def accept_cash(self, cash):
        """Discount on rebate."""
        return cash * self.rebate


class CashRetrun(CashSuper):
    """Return cash."""

    def __init__(self, threshold, money):
        """Initilize threshold and money."""
        self.threshold = threshold
        self.money = money

    def accept_cash(self, cash):
        """Discount on threshold and money."""
        return cash - int(cash / self.threshold) * self.money


class CashContext(object):
    """Basic context pattern."""

    def __init__(self, strategy):
        """Initilize with input strategy."""
        self.strategy = strategy

    def get_result(self, cash):
        """Get the final result of cash."""
        return self.strategy.accept_cash(cash)


class CashContextFactory(object):
    """Context with simple factory pattern."""

    def __init__(self, strategy_name, *args):
        """Select different strategy depends on name."""
        if strategy_name == "normal":
            self.strategy = CashNormal()
        elif strategy_name == "rebate":
            self.strategy = CashRebate(args[0])
        elif strategy_name == 'return':
            self.strategy = CashRetrun(args[0], args[1])
        else:
            print("Wrong mode!")
            self.strategy = CashSuper()

    def get_result(self, cash):
        """Get the final result of cash."""
        return self.strategy.accept_cash(cash)


if __name__ == '__main__':
    cash_context = CashContext(CashNormal())
    print(cash_context.get_result(1000))

    cash_context = CashContext(CashRebate(0.8))
    print(cash_context.get_result(1000))

    cash_context = CashContext(CashRetrun(300, 100))
    print(cash_context.get_result(1000))

    cash_context = CashContextFactory('normal')
    print(cash_context.get_result(1000))

    cash_context = CashContextFactory('rebate', 0.8)
    print(cash_context.get_result(1000))

    cash_context = CashContextFactory('return', 300, 100)
    print(cash_context.get_result(1000))
