"""Abstrat factory pattern."""

__version__ = 1.0
__date__ = "2020-08-07"


from abc import ABCMeta, abstractmethod


class User(object):
    """User class."""


class IUser(metaclass=ABCMeta):
    """Vitural base class of user."""

    @abstractmethod
    def insert(self, user):
        """Insert user into database."""
        pass

    @abstractmethod
    def get_user(self, id):
        """Get user by id."""
        pass


class SQLUser(IUser):
    """SQL user."""

    def insert(self, user):
        """Insert user into database."""
        print('SQL Server: Insert to user table.')

    def get_user(self, id):
        """Get user by id."""
        print('SQL Server: get user by id', id)


class AccessUser(IUser):
    """Access user."""

    def insert(self, user):
        """Insert user into database."""
        print('Access: Insert to user table.')

    def get_user(self, id):
        """Get user by id."""
        print('Access: get user by id', id)


class Department(object):
    """Department class."""


class IDepartment(metaclass=ABCMeta):
    """Vitural base class of department."""

    @abstractmethod
    def insert(self, department):
        """Insert department into database."""
        pass

    @abstractmethod
    def get_department(self, id):
        """Get department by id."""
        pass


class SQLDepartment(IDepartment):
    """SQL department."""

    def insert(self, department):
        """Insert department into database."""
        print('SQL Server: Insert to department table.')

    def get_department(self, id):
        """Get department by id."""
        print('SQL Server: get department by id', id)


class AccessDepartment(IDepartment):
    """Access department."""

    def insert(self, department):
        """Insert department into database."""
        print('Access: Insert to department table.')

    def get_department(self, id):
        """Get department by id."""
        print('Access: get department by id', id)


class Factory(metaclass=ABCMeta):
    """Vitural base class of factory."""

    @abstractmethod
    def create_user(self):
        """Create new user."""
        pass

    @abstractmethod
    def create_department(self):
        """Create new department."""
        pass


class SQLFactory(Factory):
    """SQL version Factory."""

    def create_user(self):
        """Create SQL version user."""
        return SQLUser()

    def create_department(self):
        """Create SQL version department."""
        return SQLDepartment()


class AccessFactory(Factory):
    """Access version Factory."""

    def create_user(self):
        """Create Access version user."""
        return AccessUser()

    def create_department(self):
        """Create Access version department."""
        return AccessDepartment()


if __name__ == '__main__':
    user = User()
    department = Department()
    factory = SQLFactory()
    # factory = AccessFactory()
    user_table = factory.create_user()
    user_table.insert(user)
    user_table.get_user(1)
    department_table = factory.create_department()
    department_table.insert(department)
    department_table.get_department(1)
