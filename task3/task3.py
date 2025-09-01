#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задача 3 (Лаборатория производительности NT):

На вход подаются:
1) values.json — id и их значения
2) tests.json — структура тестов (вложенная)
3) report.json — выходной файл

Нужно подставить значения value по id из values.json в tests.json
и сохранить как report.json.
"""

import sys
import json

def fill_values(node, values_map):
    if "id" in node and node["id"] in values_map:
        node["value"] = values_map[node["id"]]
    if "values" in node:
        for child in node["values"]:
            fill_values(child, values_map)

def main(argv):
    if len(argv) != 4:
        print("Использование: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_file, tests_file, report_file = argv[1], argv[2], argv[3]

    with open(values_file, "r", encoding="utf-8") as f:
        values_data = json.load(f)
    values_map = {item["id"]: item["value"] for item in values_data["values"]}

    with open(tests_file, "r", encoding="utf-8") as f:
        tests_data = json.load(f)

    for test in tests_data["tests"]:
        fill_values(test, values_map)

    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(tests_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main(sys.argv)
# TODO: implement
