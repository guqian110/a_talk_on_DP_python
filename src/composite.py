"""Composite pattern."""

__version__ = 1.0
__date__ = "2020-08-20"


from abc import ABCMeta, abstractmethod


class Company(metaclass=ABCMeta):
    """Vitural base class of company."""

    def __init__(self, name):
        """Initilize company name."""
        super(Company, self).__init__()
        self._name = name

    @abstractmethod
    def add(self, company):
        """Add company to children."""
        pass

    @abstractmethod
    def remove(self, company):
        """Remove company from children."""
        pass

    @abstractmethod
    def display(self, depth):
        """Display all children."""
        pass

    @abstractmethod
    def show_duty(self, depth):
        """Show duty of self."""
        pass


class ConcreteCompany(Company):
    """Concrete company."""

    def __init__(self, name):
        """Initilize company name."""
        super(ConcreteCompany, self).__init__(name)
        self._children = []

    def add(self, company):
        """Add company to children."""
        self._children.append(company)

    def remove(self, company):
        """Remove company from children."""
        self._children.remove(company)

    def display(self, depth):
        """Display all children."""
        print('*'*depth, self._name)
        for child in self._children:
            child.display(depth+2)

    def show_duty(self, depth):
        """Show duty of self."""
        for child in self._children:
            child.show_duty(depth+2)


class HRDepartment(Company):
    """HR department of company."""

    def __init__(self, name):
        """Initilize department name."""
        super(HRDepartment, self).__init__(name)

    def add(self, company):
        """Can't add company to children."""
        pass

    def remove(self, company):
        """Can't remove company from children."""
        pass

    def display(self, depth):
        """Display self."""
        print('*'*depth, self._name)

    def show_duty(self, depth):
        """Show duty of self."""
        print('*'*depth, self._name, 'human resource.')


class FinanceDepartment(Company):
    """Finance department of company."""

    def __init__(self, name):
        """Initilize department name."""
        super(FinanceDepartment, self).__init__(name)

    def add(self, company):
        """Can't add company to children."""
        pass

    def remove(self, company):
        """Can't remove company from children."""
        pass

    def display(self, depth):
        """Display self."""
        print('*'*depth, self._name)

    def show_duty(self, depth):
        """Show duty of self."""
        print('*'*depth, self._name, 'finance analysis.')


if __name__ == '__main__':
    # head quarter
    head_quarter = ConcreteCompany('Beijing HeadQuarter')
    head_quarter.add(HRDepartment('Beijing HeadQuarter HR'))
    head_quarter.add(FinanceDepartment('Beijing HeadQuarter Finance'))
    # sub company
    branch = ConcreteCompany('Shanghai Branch')
    branch.add(HRDepartment('Shanghai Branch HR'))
    branch.add(FinanceDepartment('Shanghai Branch Finance'))
    head_quarter.add(branch)
    # nanjing office
    nanjing = ConcreteCompany('Nanjing Office')
    nanjing.add(HRDepartment('Nanjing Office HR'))
    nanjing.add(FinanceDepartment('Nanjing Office Finance'))
    branch.add(nanjing)
    # hangzhou office
    hangzhou = ConcreteCompany('Hangzhou Office')
    hangzhou.add(HRDepartment('Hangzhou Office HR'))
    hangzhou.add(FinanceDepartment('Hangzhou Office Finance'))
    branch.add(hangzhou)
    # display
    head_quarter.display(1)
    # show duty
    head_quarter.show_duty(1)
