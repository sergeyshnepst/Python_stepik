"""
Вам доступен текстовый файл, в котором могут быть записаны цифры, буквы и пробелы. Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).

Напишите программу, которая принимает на вход название файла и вычисляет сумму всех чисел, записанных в нем.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести сумму всех чисел, записанных в файле.
"""

with open(input(), 'r', encoding='utf-8') as file:
    lines_list = file.readlines()
    letters = 0
    words = 0
    lines = 0 
    for line in lines_list:
        result = line.split()
        words += len(result)
        for el in line:
            if el.isalnum():
                letters += 1
        lines += 1
    print(
    f"""Input file contains:
{letters} letters
{words} words
{lines} lines"""
    )