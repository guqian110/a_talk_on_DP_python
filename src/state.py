"""State pattern."""

__version__ = 1.0
__date__ = "2020-08-19"


from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    """Vitural base class of state."""

    @abstractmethod
    def write_program(self, work):
        """Write program for work."""
        pass


class ForenoonState(State):
    """Forenoon state."""

    def write_program(self, work):
        """Write program for work."""
        if work.hour < 12:
            print("Current time:", work.hour, ", work hard!")
        else:
            work.set_state(NoonState())
            work.write_program()


class NoonState(State):
    """Noon state."""

    def write_program(self, work):
        """Write program for work."""
        if work.hour < 13:
            print("Current time:", work.hour, ", Sleeping.")
        else:
            work.set_state(AfternoonState())
            work.write_program()


class AfternoonState(State):
    """Afternoon state."""

    def write_program(self, work):
        """Write program for work."""
        if work.hour < 17:
            print("Current time:", work.hour, ", work continually!")
        else:
            work.set_state(EveningState())
            work.write_program()


class EveningState(State):
    """Evening state."""

    def write_program(self, work):
        """Write program for work."""
        if work.task_finished:
            work.set_state(RestState())
            work.write_program()
        else:
            if work.hour < 21:
                print("Current time:", work.hour, ", very tired.")
            else:
                work.set_state(SleepingState())
                work.write_program()


class SleepingState(State):
    """Sleeping state."""

    def write_program(self, work):
        """Write program for work."""
        print("Current time:", work.hour, ", go to bed.")


class RestState(State):
    """Rest state."""

    def write_program(self, work):
        """Write program for work."""
        print("Current time:", work.hour, ", go home.")


class Work(object):
    """Work of some projects."""

    def __init__(self):
        """Initilize work state and task state."""
        super(Work, self).__init__()
        self._curr_state = ForenoonState()
        self._hour = 0
        self.task_finished = False

    def set_state(self, state):
        """Set state of work."""
        self._curr_state = state

    def write_program(self):
        """Write program for this work."""
        self._curr_state.write_program(self)


if __name__ == '__main__':
    # emergency projects
    emergency_projects = Work()
    emergency_projects.hour = 9
    emergency_projects.write_program()
    emergency_projects.hour = 10
    emergency_projects.write_program()
    emergency_projects.hour = 12
    emergency_projects.write_program()
    emergency_projects.hour = 13
    emergency_projects.write_program()
    emergency_projects.hour = 14
    emergency_projects.write_program()
    emergency_projects.hour = 17
    # emergency_projects.task_finished = True
    emergency_projects.write_program()
    emergency_projects.hour = 19
    emergency_projects.write_program()
    emergency_projects.hour = 22
    emergency_projects.write_program()
