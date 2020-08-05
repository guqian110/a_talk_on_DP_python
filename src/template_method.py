"""Template pattern."""

__version__ = 1.0
__date__ = "2020-08-05"


from abc import ABCMeta, abstractmethod


class TestPaper(metaclass=ABCMeta):
    """Vitural base class of test paper."""

    def question_1(self):
        """Question 1."""
        print('Question 1: ... Answer 1: ' + self.answer_1())

    def question_2(self):
        """Question 1."""
        print('Question 2: ... Answer 2: ' + self.answer_2())

    def question_3(self):
        """Question 1."""
        print('Question 3: ... Answer 3: ' + self.answer_3())

    @abstractmethod
    def answer_1(self):
        """Answer to question 1."""
        pass

    @abstractmethod
    def answer_2(self):
        """Answer to question 2."""
        pass

    @abstractmethod
    def answer_3(self):
        """Answer to question 3."""
        pass


class TestPaperA(TestPaper):
    """Student A test paper."""

    def answer_1(self):
        """Answer to question 1."""
        return 'a'

    def answer_2(self):
        """Answer to question 2."""
        return 'b'

    def answer_3(self):
        """Answer to question 3."""
        return 'c'


class TestPaperB(TestPaper):
    """Student B test paper."""

    def answer_1(self):
        """Answer to question 1."""
        return 'b'

    def answer_2(self):
        """Answer to question 2."""
        return 'c'

    def answer_3(self):
        """Answer to question 3."""
        return 'd'


if __name__ == '__main__':
    student_a = TestPaperA()
    student_b = TestPaperB()
    print('student A:')
    student_a.question_1()
    student_a.question_2()
    student_a.question_3()
    print('Student B:')
    student_b.question_1()
    student_b.question_2()
    student_b.question_3()