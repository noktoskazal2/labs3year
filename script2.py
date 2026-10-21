import random
MAX_SIZE = 100

def sum_even_nums_in_list_static(ls: list[int]) -> int:
    total_sum = 0

    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            total_sum += ls[i]
    return total_sum


def sum_between_zeros_static(ls: list[int]) -> int:
    start = -1
    end = -1
    n = len(ls)

    for i in range(n):
        if ls[i] == 0:
            start = i
            break

    for i in range(n - 1, -1, -1):
        if ls[i] == 0:
            end = i
            break

    if start == -1 or start == end:
        return 0

    total_sum = 0
    for i in range(start + 1, end):
        total_sum += ls[i]

    return total_sum


def negative_to_start_static(ls: list[int]) -> None:
    n = len(ls)

    insert_idx = 0

    for i in range(n):
        if ls[i] < 0:

            temp = ls[i]

            for j in range(i, insert_idx, -1):
                ls[j] = ls[j - 1]

            ls[insert_idx] = temp
            insert_idx += 1


def main():
    print("Лабораторная работа: Работа со статическим")
    print(f"Максимально допустимая размерность массива {MAX_SIZE}")
    while True:
        try:
            n = int(input(f"Введите реальное количество элементов массива (от 1 до {MAX_SIZE}): "))
            if 1 <= n <= MAX_SIZE:
                break
            print(f"Ошибка! Количество элементов должно быть в диапазоне от 1 до {MAX_SIZE}.")
        except ValueError:
            print("Ошибка! Введите корректное целое число.")

    ls = [0] * n

    print("Выберите способ заполнения массива:")
    print("1. Ввод элементов вручную с клавиатуры")
    print("2. Автоматическое заполнение случайными числами")

    while True:
        choice = input("Ваш выбор (1 или 2): ").strip()
        if choice in ('1', '2'):
            break
        print("Неверный выбор. Пожалуйста, введите 1 или 2.")

    if choice == '1':
        print(f"Заполнение массива вручную ({n} элементов):")
        for i in range(n):
            while True:
                try:
                    ls[i] = int(input(f"Введите элемент [{i}]: "))
                    break
                except ValueError:
                    print("Ошибка! Введите целые числа.")
    else:
        print("\nЗаполнение датчиком случайных чисел:")
        while True:
            try:
                low = int(input("Введите нижнюю границу интервала: "))
                high = int(input("Введите верхнюю границу интервала: "))
                if low <= high:
                    break
                print("Ошибка! Нижняя граница не может быть больше верхней.")
            except ValueError:
                print("Ошибка! Границы должны быть целыми числами.")

        for i in range(n):
            ls[i] = random.randint(low, high)

    print("\n" + "=" * 50)
    print(f"исходный масив: {ls}")
    print("=" * 50)

    arr_task1 = ls.copy()
    even_sum = sum_even_nums_in_list_static(arr_task1)
    print(f"Сумма четных элементов: {even_sum}")

    arr_task2 = ls.copy()
    zeros_sum = sum_between_zeros_static(arr_task2)
    print(f"2. Сумма элементов между первыми и последним нулями: {zeros_sum}")

    arr_task3 = ls.copy()
    negative_to_start_static(arr_task3)
    print(f"3. Массив после переноса отрицательных чисел: {arr_task3}")
    print("=" * 50)


if __name__ == "__main__":
    main()







