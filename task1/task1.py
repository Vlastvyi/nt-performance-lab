#!/usr/bin/env python3
"""
Задача 1 (Лаборатория производительности NT):

Учитывая два циклических массива, неявно определенных как 1..n1 и 1..n2,
и длины интервалов m1 и m2, выведите объединенный "путь" для обоих массивов.
Путь - это последовательность начальных элементов каждого интервала длиной m,
где каждый интервал начинается с конца предыдущего интервала, и мы останавливаемся, когда
конец интервала становится равным 1 (включительно).

Использование:
    python task1.py n1 m1 n2 m2

Пример:
    питон task1.py 6 3 5 4
    -> 13514253
"""

import sys

def compute_path(n: int, m: int):
    if n <= 0 or m <= 0:
        raise ValueError("n and m must be positive integers")
    path = []
    s = 1  # start index (1-based)
    while True:
        path.append(s)
        e = ((s + m - 2) % n) + 1  # end index of current interval
        if e == 1:
            break
        s = e
    return path

def main(argv):
    if len(argv) != 5:
        print("Usage: python task1.py n1 m1 n2 m2")
        sys.exit(1)
    try:
        n1, m1, n2, m2 = map(int, argv[1:5])
    except ValueError:
        print("All arguments must be integers: n1 m1 n2 m2")
        sys.exit(1)

    try:
        p1 = compute_path(n1, m1)
        p2 = compute_path(n2, m2)
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    # Concatenate without separators to match the examples
    out = "".join(str(x) for x in p1) + "".join(str(x) for x in p2)
    print(out)

if __name__ == "__main__":
    main(sys.argv)
