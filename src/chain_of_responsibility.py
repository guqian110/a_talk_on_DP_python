"""Chain of responsibility pattern."""

__version__ = 1.0
__date__ = "2020-08-25"


from abc import ABCMeta, abstractmethod


class Request(object):
    """Request information."""

    def __init__(self, req_type, req_number):
        """Initilize request type and number."""
        super(Request, self).__init__()
        self.type = req_type
        self.number = req_number


class Manager(metaclass=ABCMeta):
    """Vitural base class of manager."""

    def __init__(self, name):
        """Initilize manager information."""
        super(Manager, self).__init__()
        self._name = name
        self._superior = None

    def set_superior(self, superior):
        """Set superior."""
        self._superior = superior

    @abstractmethod
    def request_application(self, request):
        """Resolve aplication."""
        pass


class CommonManager(Manager):
    """Common Manager."""

    def request_application(self, request):
        """Resolve aplication."""
        if request.type == 'ask for leave' and request.number <= 2:
            print(self._name, ': Approve', request.type, request.number)
        else:
            self._superior.request_application(request)


class DirectorManager(Manager):
    """Director Manager."""

    def request_application(self, request):
        """Resolve aplication."""
        if request.type == 'ask for leave' and request.number <= 5:
            print(self._name, ': Approve', request.type, request.number)
        else:
            self._superior.request_application(request)


class GeneralManager(Manager):
    """General Manager."""

    def request_application(self, request):
        """Resolve aplication."""
        if request.type == 'ask for leave':
            print(self._name, ': Approve', request.type, request.number)
        elif request.type == 'salary increasement':
            if request.number <= 500:
                print(self._name, ': Approve', request.type, request.number)
            else:
                print(self._name, ': Reject', request.type, request.number)


if __name__ == '__main__':
    # setup
    common_manager = CommonManager('JingLi')
    director_manager = DirectorManager('ZongJian')
    general_manager = GeneralManager('ZongJingLi')
    common_manager.set_superior(director_manager)
    director_manager.set_superior(general_manager)
    # request
    request1 = Request('ask for leave', 1)
    common_manager.request_application(request1)
    request2 = Request('ask for leave', 4)
    common_manager.request_application(request2)
    request3 = Request('salary increasement', 500)
    common_manager.request_application(request3)
    request4 = Request('salary increasement', 1000)
    common_manager.request_application(request4)
