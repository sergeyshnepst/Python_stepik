"""
Вам доступен текстовый файл, состоящий из нескольких строк. Напишите функцию numbering_write(), которая принимает название файла и записывает его содержимое в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 1.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Вызывать функцию numbering_write() не нужно, требуется только реализовать ее.

Примечание 3. Используйте встроенную функцию enumerate()
"""
def numbering_write(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for line in lines:
            output_file.write(f"{lines.index(line) + 1}) {line}")
        

numbering_write('zen.txt')
with open('output.txt') as f:
    print(f.read())