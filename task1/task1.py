#!/usr/bin/env python3
"""
Задача 1 (Лаборатория производительности NT):

Есть два циклических массива (от 1 до n1 и от 1 до n2).
Двигаемся по каждому из них интервалами длины m1 и m2 соответственно.
Каждый новый интервал начинается с конца предыдущего.
Останавливаемся, когда конец интервала равен 1.
Путь — это последовательность начальных элементов интервалов.

Пример запуска:
    python task1.py 6 3 5 4
"""

import sys

def compute_intervals_and_path(n: int, m: int):
    if n <= 0 or m <= 0:
        raise ValueError("n и m должны быть положительными числами")
    intervals = []
    path = []
    s = 1
    while True:
        path.append(s)
        # Строим интервал длиной m
        interval = []
        for i in range(m):
            interval.append(((s - 1 + i) % n) + 1)
        intervals.append(interval)
        e = interval[-1]  # конец интервала
        if e == 1:
            break
        s = e
    return intervals, path

def main(argv):
    if len(argv) != 5:
        print("Использование: python task1.py n1 m1 n2 m2")
        sys.exit(1)

    try:
        n1, m1, n2, m2 = map(int, argv[1:5])
    except ValueError:
        print("Ошибка: все аргументы должны быть целыми числами")
        sys.exit(1)

    # Массив 1
    intervals1, path1 = compute_intervals_and_path(n1, m1)
    print(f"Массив 1: n = {n1}, m = {m1}")
    print(f"Круговой массив: {''.join(str(i) for i in range(1, n1+1))}.")
    print(f"При длине обхода {m1} получаем интервалы: " +
          ", ".join("".join(str(x) for x in it) for it in intervals1) + ".")
    print(f"Полученный путь: {''.join(str(x) for x in path1)}.\n")

    # Массив 2
    intervals2, path2 = compute_intervals_and_path(n2, m2)
    print(f"Массив 2: n = {n2}, m = {m2}")
    print(f"Круговой массив: {''.join(str(i) for i in range(1, n2+1))}.")
    print(f"При длине обхода {m2} получаем интервалы: " +
          ", ".join("".join(str(x) for x in it) for it in intervals2) + ".")
    print(f"Полученный путь: {''.join(str(x) for x in path2)}.\n")

    # Итоговый вывод
    result = "".join(str(x) for x in path1) + "".join(str(x) for x in path2)
    print(f"В этом примере на вход подаются аргументы: {n1} {m1} и {n2} {m2}, "
          f"ожидаемый вывод в консоль: {result}")

if __name__ == "__main__":
    main(sys.argv)
