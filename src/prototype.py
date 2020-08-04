"""Prototype pattern."""

__version__ = 1.0
__date__ = "2020-08-04"

from copy import deepcopy


class WorkExperience(object):
    """Work experience."""

    def __init__(self):
        """Init work date."""
        self._work_date = ''
        self._company = ''


class Resume(object):
    """Resume class."""

    def __init__(self, name):
        """Initilize basic information."""
        self._name = name
        self._work_experience = WorkExperience()

    def set_personal_info(self, sex, age):
        """Set personal information."""
        self._sex = sex
        self._age = age

    def set_work_experience(self, work_date, company):
        """Set work experience information."""
        self._work_experience._work_date = work_date
        self._work_experience._company = company

    def display(self):
        """Display all informations."""
        print(self._name, self._sex, self._age)
        print(self._work_experience._work_date, self._work_experience._company)

    def clone(self):
        """Uisng deep copy to clone."""
        new_resume = deepcopy(self)
        new_resume._work_experience = deepcopy(self._work_experience)
        return new_resume


if __name__ == '__main__':
    # add
    resume = Resume('Tom')
    resume.set_personal_info('male', '30')
    resume.set_work_experience('2019', 'Google')
    new_resume = resume.clone()
    new_resume.set_personal_info('female', '25')
    new_resume.set_work_experience('2020', 'Apple')
    resume.display()
    new_resume.display()
