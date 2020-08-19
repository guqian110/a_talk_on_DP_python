"""Memento pattern."""

__version__ = 1.0
__date__ = "2020-08-19"


class GameRole(object):
    """originator: game role."""

    def __init__(self):
        """Initilize role state."""
        super(GameRole, self).__init__()
        self._vitality = 0
        self._attack = 0
        self._defence = 0

    def display_state(self):
        """Dislay role state."""
        print("Role's current state:")
        print("vitality:", self._vitality)
        print("attack:", self._attack)
        print("defence:", self._defence)

    def get_init_state(self):
        """Get initial role state."""
        self._vitality = 100
        self._attack = 100
        self._defence = 100

    def fight(self):
        """Update role state after fight."""
        self._vitality = 0
        self._attack = 0
        self._defence = 0

    def save_state(self):
        """Save role state into memento."""
        return RoleStateMemento(self._vitality, self._attack, self._defence)

    def recove_state(self, memento):
        """Recove role state from memento."""
        self._vitality = memento._vitality
        self._attack = memento._attack
        self._defence = memento._defence


class RoleStateMemento(object):
    """Memento for role state."""

    def __init__(self, vitality, attack, defence):
        """Save role state."""
        super(RoleStateMemento, self).__init__()
        self._vitality = vitality
        self._attack = attack
        self._defence = defence


class RoleStateCaretaker(object):
    """Caretaker for role state."""

    def __init__(self, memento):
        """Save role state into a memento."""
        super(RoleStateCaretaker, self).__init__()
        self._memento = memento

    def get_memento(self):
        """Return memento."""
        return self._memento


if __name__ == '__main__':
    # before fight with the boss
    lixiaoyao = GameRole()
    lixiaoyao.get_init_state()
    lixiaoyao.display_state()
    # save
    state_admin = RoleStateCaretaker(lixiaoyao.save_state())
    # fight
    lixiaoyao.fight()
    lixiaoyao.display_state()
    # recovery
    lixiaoyao.recove_state(state_admin.get_memento())
    lixiaoyao.display_state()
