"""Simple factory pattern."""

__version__ = 1.0
__date__ = "2020-07-08"


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

    def create_operation(self, op):
        """Create different opreations."""
        if op == "+":
            operation = OperationAdd()
        elif op == "-":
            operation = OperationSub()
        elif op == "*":
            operation = OperationMult()
        elif op == "/":
            operation = OperationDiv()
        else:
            print("Invalid operator!")
            operation = None
        return operation


if __name__ == '__main__':
    operator = input("operator: ")
    fectory = OperationFactory()
    operation = fectory.create_operation(operator)
    operation.num_a = float(input("num a: "))
    operation.num_b = float(input("num b: "))
    print(operation.get_result())
