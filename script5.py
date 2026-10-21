def get_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(f"{prompt}: "))
            if value <= 0:
                print("Ошибка! Число должно быть больше нуля")
                continue
            return value
        except ValueError:
            print("Ошибка! Введите целое положительное число")


class Person:
    def __init__(self, name: str):
        self.name = name
        print(f"[Person] Вызван конструктор для {self.name}")

    def __del__(self):
        print(f"[Person] Вызван деструктор для {self.name}")

    def get_name(self):
        return self.name

    def set_name(self,name: str):
        self.name = name

    def display_info(self):
        print(f"Имя {self.name}")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"

class Student(Person):
    def __init__(self, name: str, course: int, group: int):
        super().__init__(name)
        self.course = course
        self.group = group
        print(f"[Student] Вызван конструктор для {self.name}")

    def __del__(self):
        print(f"[Student] Вызван деструктор для {self.name}")
        super().__del__()

    def get_course(self):
        return self.course

    def get_group(self):
        return self.group

    def set_course(self,course: int):
        self.course = course

    def set_group(self,group: int):
        self.group = group

    def display_info(self):
        super().display_info()
        print(f"Курс {self.course}, группа {self.group}")


class Professor(Person):
    def __init__(self, name: str, department: str):
        super().__init__(name)
        self.department = department
        print(f"[Professor] Вызван конструктор для {self.name}")

    def __del__(self):
        print(f"[Professor] Вызван деструктор для {self.name}")
        super().__del__()

    def get_department(self):
        return self.department

    def set_department(self,department: str):
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Кафедра {self.department}")

if __name__ == "__main__":
    ls = []
    while True:
        print("Выберите один из Пунктов")
        print("1) Ввести студента")
        print("2) Ввести преподователя")
        print("3)Вывести список студентов")
        print("4) Вывести список преподователей")
        print("5) Закончить Работу")
        choice = input()
        if choice in ['1', '2', '3', '4','5']:
            choice = int(choice)
        else:
            print(f"вы ввели неккоректный пункт {choice} попробуйте заного")
            continue
        if choice == 1:
           name = input("Введите имя студента")
           course = get_positive_int("Введите номер курса")
           group = get_positive_int("Введите номер группы")
           ls.append(Student(name, course, group))
        if choice == 2:
            name = input("Введите имя преподователя")
            department = input("Введите название кафедры")
            ls.append(Professor(name, department))
        if choice == 3:
            print([p for p in ls if isinstance(p,Student)])
        if choice == 4:
            print ([p for p in ls if isinstance(p,Professor)])
        if choice == 5:
            break









