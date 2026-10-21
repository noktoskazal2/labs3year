import random


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


def get_any_int(prompt: str) -> int:
    while True:
        try:
            return int(input(f"{prompt}: "))
        except ValueError:
            print("Ошибка! Введите целое число.\n")


def is_positive_in_list(lst: list[int]) -> bool:
    for num in lst:
        if num > 0:
            return True
    return False


def max_element_in_cals_where_elements_is_not_positive(mtr: list[list[int]]) -> list[int]:

    if not mtr or not mtr[0]:
        return []

    rows_cnt = len(mtr)
    cols_cnt = len(mtr[0])
    max_elements = []

    for col_ind in range(cols_cnt):
        column = [mtr[row_ind][col_ind] for row_ind in range(rows_cnt)]

        if not is_positive_in_list(column):
            max_elements.append(max(column))

    return max_elements


def number_negative_nums_in_lower_right_triangle(mtr: list[list[int]]) -> int:

    n = len(mtr)
    counter = 0

    for i in range(n):
        for j in range(n):
            if i + j >= n - 1 and mtr[i][j] < 0:
                counter += 1

    return counter


def main():
    print("Тест лабораторной работы")

    while True:
        print("Как вы хотите заполнить массив?")
        print("1. Вручную")
        print("2. Случайно")
        choise = input("Введите выбор (1 или 2): ").strip()

        if choise in ['1', '2']:
            choise = int(choise)
            break
        print("Ошибка! Вы должны ввести 1 или 2.")

    mtr = []

    if choise == 1:
        rows = get_positive_int("Введите количество строк")
        cols = get_positive_int("Введите количество столбцов")

        for row_ind in range(rows):
            row = []
            for col_ind in range(cols):
                element = get_any_int(f"Введите элемент {row_ind + 1} строки {col_ind + 1} столбца")
                row.append(element)
            mtr.append(row)

    elif choise == 2:
        rows = get_positive_int("Введите количество строк")
        cols = get_positive_int("Введите количество столбцов")
        a = get_any_int("Введите минимальное случайное число возможное в генераторе")
        b = get_any_int("Введите максимальное случайное число возможное в генераторе")
        if a < b:
            a,b = b,a

        for row_ind in range(rows):
            row = [random.randint(a,b) for _ in range(cols)]
            mtr.append(row)

    print("Ваша матрица:")
    for row in mtr:
        print(row)

    print("Проверка функций из лабораторной работы:")

    print("1. Максимальные элементы в столбцах без положительных элементов:")
    max_in_cols = max_element_in_cals_where_elements_is_not_positive(mtr)
    print(f"   Результат: {max_in_cols}")

    print("2. Количество отрицательных элементов в нижнем правом треугольнике:")
    if rows != cols:
        print("   Ошибка: вторая функция требует квадратную матрицу, а ваша не квадратная!")
    else:
        neg_count = number_negative_nums_in_lower_right_triangle(mtr)
        print(f"   Результат: {neg_count}")


if __name__ == "__main__":
    main()