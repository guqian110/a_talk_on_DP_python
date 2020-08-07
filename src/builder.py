"""Builder pattern."""

__version__ = 1.0
__date__ = "2020-08-07"


from abc import ABCMeta, abstractmethod


class PersonBuilder(metaclass=ABCMeta):
    """Vitural base class to build a person."""

    @abstractmethod
    def build_head(self):
        """Build head of a person."""
        pass

    @abstractmethod
    def build_body(self):
        """Build body of a person."""
        pass

    @abstractmethod
    def build_left_arm(self):
        """Build left arm of a person."""
        pass

    @abstractmethod
    def build_right_arm(self):
        """Build right arm of a person."""
        pass

    @abstractmethod
    def build_left_leg(self):
        """Build left leg of a person."""
        pass

    @abstractmethod
    def build_right_leg(self):
        """Build left leg of a person."""
        pass


class PersonThinBuilder(PersonBuilder):
    """Thin person builder."""

    def build_head(self):
        """Build head of a person."""
        print('Build thin head.')

    def build_body(self):
        """Build body of a person."""
        print('Build thin body.')

    def build_left_arm(self):
        """Build left arm of a person."""
        print('Build thin left arm.')

    def build_right_arm(self):
        """Build right arm of a person."""
        print('Build thin right arm.')

    def build_left_leg(self):
        """Build left leg of a person."""
        print('Build thin left leg.')

    def build_right_leg(self):
        """Build left leg of a person."""
        print('Build thin right leg.')


class PersonFatBuilder(PersonBuilder):
    """Fat person builder."""

    def build_head(self):
        """Build head of a person."""
        print('Build fat head.')

    def build_body(self):
        """Build body of a person."""
        print('Build fat body.')

    def build_left_arm(self):
        """Build left arm of a person."""
        print('Build fat left arm.')

    def build_right_arm(self):
        """Build right arm of a person."""
        print('Build fat right arm.')

    def build_left_leg(self):
        """Build left leg of a person."""
        print('Build fat left leg.')

    def build_right_leg(self):
        """Build left leg of a person."""
        print('Build fat right leg.')


class PersonDirector(object):
    """Director to build a person."""

    def __init__(self, builder):
        """Initilize a builder."""
        super(PersonDirector, self).__init__()
        self._person_builder = builder

    def create_person(self):
        """Create a new person."""
        self._person_builder.build_head()
        self._person_builder.build_body()
        self._person_builder.build_left_arm()
        self._person_builder.build_right_arm()
        self._person_builder.build_left_leg()
        self._person_builder.build_right_leg()


if __name__ == '__main__':
    # build thin person
    person_thin_builder = PersonThinBuilder()
    person_director = PersonDirector(person_thin_builder)
    person_director.create_person()
    # build fat person
    person_fat_builder = PersonFatBuilder()
    person_director = PersonDirector(person_fat_builder)
    person_director.create_person()
