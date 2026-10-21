from typing import List
from students import Student, StudentAfterFirstSession, StudentAfterSecondSession

def get_group_avg_first_session(students: List[Student], target_group: int) -> float:
    scores = []
    for s in students:
        if isinstance(s, StudentAfterFirstSession) and s.group == target_group:
            avg_s1 = sum(s.grades_s1) / len(s.grades_s1)
            scores.append(avg_s1)

    return sum(scores) / len(scores) if scores else 0.0

def get_group_avg_year(students: List[Student], target_group: int) -> float:
    scores = []
    for s in students:
        if isinstance(s, StudentAfterSecondSession) and s.group == target_group:
            scores.append(s.get_average_grade())

    return sum(scores) / len(scores) if scores else 0.0


if __name__ == "__main__":
    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССОВ ===\n")

    s1 = StudentAfterFirstSession("Алексей Изотов", 1, 101, "ЗБ-2024-01", [4, 5, 4, 5])
    s2 = StudentAfterSecondSession("Мария Сидорова", 1, 101, "ЗБ-2024-02", [5, 5, 5, 5], [4, 4, 5, 5, 5])
    s3 = StudentAfterSecondSession("Иван Петров", 1, 101, "ЗБ-2024-03", [3, 4, 3, 4], [3, 3, 4, 4, 3])

    s2_copy = StudentAfterSecondSession.copy(s2)

    students_list = [s1, s2, s3, s2_copy]
    for st in students_list:
        print(st)

    print("РАБОТА С МЕТОДАМИ И ОЦЕНКАМИ")
    print(f"Старая оценка s1 по 1 предмету: {s1.get_grade_s1(0)}")
    s1.set_grade_s1(0, 5)
    print(f"Новая оценка s1 по 1 предмету: {s1.get_grade_s1(0)}")

    print("РАСЧЕТ СРЕДНИХ БАЛЛОВ ПО ГРУППЕ 101")
    avg_s1_group = get_group_avg_first_session(students_list, 101)
    avg_year_group = get_group_avg_year(students_list, 101)

    print(f"Средний балл группы 101 после 1-й сессии: {avg_s1_group:.2f}")
    print(f"Средний балл группы 101 за весь год (после 2 сессий): {avg_year_group:.2f}")