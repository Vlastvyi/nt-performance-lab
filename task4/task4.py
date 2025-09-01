#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задача 4 (Лаборатория производительности NT):

Привести все элементы массива к одному числу минимальным количеством ходов (±1).
- Числа читаются из файла (по одному в строке).
- Ограничение: максимум 20 ходов.
"""

import sys

def min_moves(nums):
    nums.sort()
    n = len(nums)
    median = nums[n // 2] if n % 2 == 1 else nums[n // 2]
    return sum(abs(x - median) for x in nums)

def main(argv):
    if len(argv) != 2:
        print("Использование: python task4.py numbers.txt")
        sys.exit(1)

    filename = argv[1]
    with open(filename, "r", encoding="utf-8") as f:
        nums = [int(line.strip()) for line in f if line.strip()]

    moves = min_moves(nums)
    if moves > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    else:
        print(moves)

if __name__ == "__main__":
    main(sys.argv)
# TODO: implement
