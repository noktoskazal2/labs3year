import math

def numISDifferent(num: int) -> bool:
    mask = 0
    n = abs(num)

    if n == 0:
        return True

    while n > 0:
        digit = n % 10
        if mask & (1 << digit) != 0:
            return False
        mask |= (1 << digit)
        n //= 10
    return True

def isSimple(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5,math.isqrt(num) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def simpleLowerThenNum(num: int) -> None:
    for i in range (2, num + 1):
        if isSimple(i) == True:
            print(i)

def allNumDellimiters(num: int) -> list[int]:
    if num < 0:
        return []
    delims = []
    d = 1
    while d * d <= num:
        if num % d == 0:
            delims.append(d)
            if d * d != num:
                delims.append(num // d)
        d += 1
    return sorted(delims)

def isPerfect(num: int ) -> bool:
    if sum(allNumDellimiters(num)) ==  2 * num:
        return True
    else:
        return False

def perfectNumInSegment(a : int, b : int ) -> None:
    if a > b:
        a, b = b, a
    for i in range (a, b + 1):
        if isPerfect(i) == True:
            print(i)

def can_form_from_num(a : int, b : int) -> bool:
    a,b = abs(a),abs(b)
    if a > b:
        return False
    if a == b:
        return True
    while a > 0 and b > 0:
        if a % 10 == b % 10:
            a //= 10
        b //= 10
    return a == 0


def main():
    print("Тестирование Функций")

    print("Тест numISDifferent:")
    print("Введите число и функция скажет ращличны ли его цифры")
    test1num = int(input())
    if numISDifferent(test1num) == True:
        print("различны")
    else:
        print("не различны")

    print("Тест simpleLowerThenNum")
    print("Введите число и функция покажет все простые числа не превышающие ваше")
    test2num = int(input())
    simpleLowerThenNum(test2num)

    print("Тест perfectNumInSegment (введите промежуток из двух чисел и функция покажет совершенные среди них")
    test_a, test_b = int(input()),int(input())
    perfectNumInSegment(test_a, test_b)

    print("Тест can_form_from_num введите два числа и функция покажет можно ли получить первое из второго путем вычеркивания чисел из второго")
    test2_a, test2_b = int(input()),int(input())
    print(f"Можно ли получить {test2_a} из {test2_b} вычеркиванием? -> {can_form_from_num(test2_a,test2_b)}")


if __name__ == '__main__':
    main()
