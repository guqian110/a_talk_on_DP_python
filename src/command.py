"""Command pattern."""

__version__ = 1.0
__date__ = "2020-08-24"


from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """Vitural base class of command."""

    def __init__(self, chef):
        """Initilize chef to execute command."""
        super(Command, self).__init__()
        self._chef = chef

    @abstractmethod
    def execute(self):
        """Execute command."""
        pass


class BakeMuttonCommand(Command):
    """Bake mutton."""

    def execute(self):
        """Execute bake mutton command."""
        self._chef.bake_mutton()


class BakeChickenWingCommand(Command):
    """Bake chicken wings."""

    def execute(self):
        """Execute bake chicken wings command."""
        self._chef.bake_chicken_wing()


class Chef(object):
    """brand."""

    def bake_mutton(self):
        """Bake mutton."""
        print('Bake mutton!')

    def bake_chicken_wing(self):
        """Bake mutton."""
        print('Bake chicken wings!')


class Waiter(object):
    """Waiter of the restaurant."""

    def __init__(self):
        """Waiter has no commands."""
        super(Waiter, self).__init__()
        self._commands = []

    def set_order(self, command):
        """Set order of guests."""
        if isinstance(command, BakeChickenWingCommand):
            print('Chicken wings sold out.')
        else:
            self._commands.append(command)
            print('Add order: ', type(command).__name__)

    def cancel_order(self, command):
        """Cancel order."""
        self._commands.remove(command)
        print('Cancel order:', type(command).__name__)

    def notify(self):
        """Notify chef to execute commands."""
        for command in self._commands:
            command.execute()


if __name__ == '__main__':
    # Prepare
    chef = Chef()
    bake_mutton_command1 = BakeMuttonCommand(chef)
    bake_mutton_command2 = BakeMuttonCommand(chef)
    bake_chicken_wing_command = BakeChickenWingCommand(chef)
    waiter = Waiter()
    # Order
    waiter.set_order(bake_mutton_command1)
    waiter.set_order(bake_mutton_command2)
    waiter.set_order(bake_chicken_wing_command)
    waiter.notify()
