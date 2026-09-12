"""
Напишите программу, которая принимает на вход название файла и выводит количество строк этого файла.
"""

with open(input(), 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines_count = len(lines)
    print(lines_count)


