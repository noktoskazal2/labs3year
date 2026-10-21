from itertools import count
from typing import List

class Student:
    _counter = count(1)

    def __init__(self, name: str, course: int, group: int, record_book: str):
        self._name = name
        self._course = course
        self._group = group
        self._record_book = record_book
        self._id = next(Student._counter)  # Уникальный ID

    @property
    def id(self) -> int:
        return self._id

    @property
    def record_book(self) -> str:
        return self._record_book

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def course(self) -> int:
        return self._course

    @course.setter
    def course(self, value: int):
        self._course = value

    @property
    def group(self) -> int:
        return self._group

    @group.setter
    def group(self, value: int):
        self._group = value

    @classmethod
    def copy(cls, other: 'Student'):
        return cls(other.name, other.course, other.group, other.record_book)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ID: {self.id} | {self.name} | Курс: {self.course} | Группа: {self.group} | Зачетка: {self.record_book}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name='{self.name}')"


class StudentAfterFirstSession(Student):
    def __init__(self, name: str, course: int, group: int, record_book: str, grades_s1: List[int]):
        super().__init__(name, course, group, record_book)
        if len(grades_s1) != 4:
            raise ValueError("Оценок за 1 сессию должно быть ровно 4!")
        self._grades_s1 = list(grades_s1)

    def get_grade_s1(self, index: int) -> int:
        return self._grades_s1[index]

    def set_grade_s1(self, index: int, value: int):
        if not (2 <= value <= 5):
            raise ValueError("Оценка должна быть от 2 до 5")
        self._grades_s1[index] = value

    @property
    def grades_s1(self) -> List[int]:
        return self._grades_s1.copy()

    # Полиморфный метод: средний балл за 1 сессию
    def get_average_grade(self) -> float:
        return sum(self._grades_s1) / len(self._grades_s1)

    @classmethod
    def copy(cls, other: 'StudentAfterFirstSession'):
        return cls(other.name, other.course, other.group, other.record_book, other.grades_s1)

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} | 1 сессия: {self._grades_s1} (Ср.балл: {self.get_average_grade():.2f})"


class StudentAfterSecondSession(StudentAfterFirstSession):
    def __init__(self, name: str, course: int, group: int, record_book: str, grades_s1: List[int], grades_s2: List[int]):
        super().__init__(name, course, group, record_book, grades_s1)
        if len(grades_s2) != 5:
            raise ValueError("Оценок за 2 сессию должно быть ровно 5!")
        self._grades_s2 = list(grades_s2)

    # Методы доступа к оценкам 2 сессии
    def get_grade_s2(self, index: int) -> int:
        return self._grades_s2[index]

    def set_grade_s2(self, index: int, value: int):
        if not (2 <= value <= 5):
            raise ValueError("Оценка должна быть от 2 до 5")
        self._grades_s2[index] = value

    @property
    def grades_s2(self) -> List[int]:
        return self._grades_s2.copy()

    def get_average_grade(self) -> float:
        all_grades = self._grades_s1 + self._grades_s2
        return sum(all_grades) / len(all_grades)

    @classmethod
    def copy(cls, other: 'StudentAfterSecondSession'):
        return cls(other.name, other.course, other.group, other.record_book, other.grades_s1, other.grades_s2)

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} | 2 сессия: {self._grades_s2} (Ср.балл за год: {self.get_average_grade():.2f})"