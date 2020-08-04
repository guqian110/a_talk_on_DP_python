"""Factory pattern."""

__version__ = 1.0
__date__ = "2020-08-04"


from abc import ABCMeta, abstractmethod


class Operation(metaclass=ABCMeta):
    """Vitural base class for all operations."""

    def __init__(self):
        """Init operands."""
        self.num_a = 0
        self.num_b = 0

    @abstractmethod
    def get_result(self):
        """Get operation result."""
        pass


class OperationAdd(Operation):
    """Addition."""

    def get_result(self):
        """Get result of addition."""
        return self.num_a + self.num_b


class OperationSub(Operation):
    """Substraction."""

    def get_result(self):
        """Get result of substraction."""
        return self.num_a - self.num_b


class OperationMult(Operation):
    """Multiplication."""

    def get_result(self):
        """Get result of multiplication."""
        return self.num_a * self.num_b


class OperationDiv(Operation):
    """Division."""

    def get_result(self):
        """Get result of division."""
        try:
            result = self.num_a / self.num_b
            return result
        except ZeroDivisionError:
            print("Error: divide by zero!")
            return None


class OperationFactory(object):
    """Factory to create operations."""

    def create_operation(self):
        """Virtual method to create operations."""
        pass


class AddFactory(OperationFactory):
    """Factory for OperationAdd."""

    def create_operation(self):
        """Create add operaton."""
        return OperationAdd()


class SubFactory(OperationFactory):
    """Factory for OperationSub."""

    def create_operation(self):
        """Create sub operaton."""
        return OperationSub()


class MultFactory(OperationFactory):
    """Factory for OperationMult."""

    def create_operation(self):
        """Create mult operaton."""
        return OperationMult()


class DivFactory(OperationFactory):
    """Factory for OperationDiv."""

    def create_operation(self):
        """Create div operaton."""
        return OperationDiv()


if __name__ == '__main__':
    # add
    factory = AddFactory()
    operation = factory.create_operation()
    operation.num_a = 3
    operation.num_b = 5
    print(operation.get_result())
    # mult
    operation_factory = MultFactory()
    operation = operation_factory.create_operation()
    operation.num_a = 3
    operation.num_b = 5
    print(operation.get_result())
