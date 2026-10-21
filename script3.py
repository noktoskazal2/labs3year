import random

def sum_even_nums_in_list(ls: list[int]) -> int:
    return sum(x for x in ls if x % 2 == 0)


def sum_between_zeros(ls: list[int]) -> int:
    if 0 not in ls:
        return 0

    start = ls.index(0)

    zero_indices = [i for i, x in enumerate(ls) if x == 0]
    end = zero_indices[-1]

    if end == start:
        return 0
    else:
        return sum(ls[start + 1:end])


def negative_to_start(ls: list[int]) -> None:
    ls[:] = [x for x in ls if x < 0] + [x for x in ls if x >= 0]

def main():
    print("Лабораторная работа: Работа с динамическим массивом")

    while True:
        try:
            n = int(input("Введите количество элементов динамического массива (минимум 1): "))
            if n >= 1:
                break
            print("Ошибка! Массив должен состоять не менее, чем из одного элемента.")
        except ValueError:
            print("Ошибка! Введите корректное целое число.")

    ls = []

    print("Выберите способ заполнения массива:")
    print("1. Ввод элементов вручную с клавиатуры")
    print("2. Автоматическое заполнение случайными числами")

    while True:
        choice = input("Ваш выбор (1 или 2): ").strip()
        if choice in ('1', '2'):
            break
        print("Неверный выбор. Пожалуйста, введите 1 или 2.")

    if choice == '1':
        print(f"\nЗаполнение массива вручную ({n} элементов):")
        for i in range(n):
            while True:
                try:
                    val = int(input(f"Введите элемент [{i}]: "))
                    ls.append(val)  # В динамический массив добавляем через .append()
                    break
                except ValueError:
                    print("Ошибка Введите целое число.")
    else:
        print("Заполнение датчиком случайных чисел:")
        while True:
            try:
                low = int(input("Введите нижнюю границу интервала: "))
                high = int(input("Введите верхнюю границу интервала: "))
                if low <= high:
                    break
                print("Ошибка! Нижняя граница не может быть больше верхней.")
            except ValueError:
                print("Ошибка! Границы должны быть целыми числами.")

        for _ in range(n):
            ls.append(random.randint(low, high))

    print(f"исходный массив: {ls}")

    arr_task1 = ls.copy()
    even_sum = sum_even_nums_in_list(arr_task1)
    print(f"1. Сумма четных элементов: {even_sum}")

    arr_task2 = ls.copy()
    zeros_sum = sum_between_zeros(arr_task2)
    print(f"2. Сумма элементов между первыми и последним нулями: {zeros_sum}")

    arr_task3 = ls.copy()
    negative_to_start(arr_task3)
    print(f"3. Массив после переноса отрицательных чисел: {arr_task3}")

if __name__ == "__main__":
    main()
