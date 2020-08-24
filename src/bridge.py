"""Bridge pattern."""

__version__ = 1.0
__date__ = "2020-08-24"


from abc import ABCMeta, abstractmethod


class HandsetSoft(metaclass=ABCMeta):
    """Vitural base class of handset."""

    @abstractmethod
    def run(self, company):
        """Run handset software."""
        pass


class HandsetGame(HandsetSoft):
    """Game software."""

    def run(self):
        """Run game software."""
        print('Run Game.')


class HandsetAddressList(HandsetSoft):
    """Address list software."""

    def run(self):
        """Run address list software."""
        print('Run Address list.')


class HandsetBrand(metaclass=ABCMeta):
    """Vitural base class of handset brand."""

    def __init__(self, software):
        """Initilize handset brand."""
        super(HandsetBrand, self).__init__()
        self._software = software

    @abstractmethod
    def run(self):
        """Virtual base method of run software."""
        pass


class HandsetBrandM(HandsetBrand):
    """HandsetBrand M."""

    def run(self):
        """Run software on brand M."""
        print('Run software on M.')
        self._software.run()


class HandsetBrandN(HandsetBrand):
    """HandsetBrand N."""

    def run(self):
        """Run software on brand N."""
        print('Run software on N.')
        self._software.run()


if __name__ == '__main__':
    # brand M
    brand_m = HandsetBrandM(HandsetGame())
    brand_m.run()
    brand_m = HandsetBrandM(HandsetAddressList())
    brand_m.run()
    # brand N
    brand_n = HandsetBrandN(HandsetGame())
    brand_n.run()
    brand_n = HandsetBrandN(HandsetAddressList())
    brand_n.run()
