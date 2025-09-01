#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задача 2 (Лаборатория производительности NT):

Программа определяет положение точек относительно эллипса.
- Первый файл: координаты центра (x0, y0) и радиусы (a, b).
- Второй файл: список точек (x, y).
Вывод:
0 — точка на границе
1 — точка внутри
2 — точка снаружи
"""

import sys
from decimal import Decimal, getcontext

# увеличиваем точность вычислений
getcontext().prec = 50

def point_position(x0, y0, a, b, x, y):
    expr = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)
    if expr == 1:
        return 0
    elif expr < 1:
        return 1
    else:
        return 2

def main(argv):
    if len(argv) != 3:
        print("Использование: python task2.py ellipse.txt points.txt")
        sys.exit(1)

    ellipse_file, points_file = argv[1], argv[2]

    # читаем эллипс
    with open(ellipse_file, "r", encoding="utf-8") as f:
        x0, y0 = map(Decimal, f.readline().split())
        a, b = map(Decimal, f.readline().split())

    # читаем точки
    with open(points_file, "r", encoding="utf-8") as f:
        points = [tuple(map(Decimal, line.split())) for line in f if line.strip()]

    # проверяем каждую точку
    for (x, y) in points:
        res = point_position(x0, y0, a, b, x, y)
        print(res)

if __name__ == "__main__":
    main(sys.argv)
