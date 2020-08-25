"""Flyweight pattern."""

__version__ = 1.0
__date__ = "2020-08-25"


from abc import ABCMeta, abstractmethod


class User(object):
    """User class."""

    def __init__(self, name):
        """User has self name."""
        super(User, self).__init__()
        self.name = name


class WebSite(metaclass=ABCMeta):
    """Vitural base class of website."""

    @abstractmethod
    def use(self, user):
        """Use website with different user."""
        pass


class ConcretWebSite(WebSite):
    """Concret website."""

    def __init__(self, name):
        """Use website by different user."""
        super(ConcretWebSite, self).__init__()
        self._name = name

    def use(self, user):
        """Use website with different user."""
        print('Web category:', self._name, 'User: ', user.name)


class WebSiteFactory(object):
    """Factory to product websites."""

    def __init__(self):
        """Initialize using empty dict."""
        super(WebSiteFactory, self).__init__()
        self._flyweights = {}

    def get_website_category(self, name):
        """Get website category by name."""
        if name not in self._flyweights.keys():
            self._flyweights[name] = ConcretWebSite(name)
        return self._flyweights[name]

    def get_website_count(self):
        """Get total website number."""
        print(len(self._flyweights.keys()))


if __name__ == '__main__':
    website_factory = WebSiteFactory()
    peter = User('Pepter')
    tom = User('Tom')
    # bbs
    website = website_factory.get_website_category('bbs')
    website.use(peter)
    website.use(tom)
    website_factory.get_website_count()
    # blog
    website = website_factory.get_website_category('blog')
    website.use(peter)
    website.use(tom)
    website_factory.get_website_count()
    # bbs
    website = website_factory.get_website_category('bbs')
    website.use(peter)
    website.use(tom)
    website_factory.get_website_count()
