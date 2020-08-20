"""Singleton pattern."""

__version__ = 1.0
__date__ = "2020-08-20"


def singleton(cls, *args, **kw_args):
    """Singleton decoretor."""
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw_args)
        return instances[cls]
    return _singleton


@singleton
class MyClass(object):
    """My test class."""

    def __init__(self, arg=0):
        """Initilize arg."""
        self.arg = arg


if __name__ == '__main__':
    object_1 = MyClass()
    object_2 = MyClass()
    print(id(object_1))
    print(id(object_2))
    print(object_1 == object_2)
    print(object_1 is object_2)
    object_1.arg = 2
    print(object_2.arg)
