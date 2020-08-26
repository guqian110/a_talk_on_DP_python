"""Interpreter pattern."""

__version__ = 1.0
__date__ = "2020-08-26"


from abc import ABCMeta, abstractmethod


class Context(object):
    """Context class."""

    def __init__(self, text):
        """Initialize Context."""
        super(Context, self).__init__()
        self.text = text


class Expression(metaclass=ABCMeta):
    """Vitural base class of expression."""

    def interpret(self, context):
        """Interprete context."""
        text = context.text.split(' ')
        key = text[0]
        value = float(text[1])
        context.text = ' '.join(text[2:])
        self.execute(key, value)

    @abstractmethod
    def execute(self, key, value):
        """Execute expressions."""
        pass


class Note(Expression):
    """Note class."""

    def execute(self, key, value):
        """Execute notes."""
        if key == 'C':
            note = 1
        elif key == 'D':
            note = 2
        elif key == 'E':
            note = 3
        elif key == 'F':
            note = 4
        elif key == 'G':
            note = 5
        elif key == 'A':
            note = 6
        elif key == 'B':
            note = 7
        print(note)


class Scale(Expression):
    """Scale class."""

    def execute(self, key, value):
        """Execute scale."""
        scale_dict = {1: 'bass', 2: 'alto', 3: 'treble'}
        print(scale_dict[value])


class ExpressionFactory(object):
    """Factory to product Expressions."""

    @staticmethod
    def create_expression(text):
        """Create expression using text."""
        type = 'Scale' if text == 'O' else 'Note'
        obj = globals()[type]()
        return obj


if __name__ == '__main__':
    context = Context('O 2 E 0.5 G 0.5 A 3 E 0.5')
    while len(context.text):
        expression = ExpressionFactory.create_expression(context.text[0])
        expression.interpret(context)
