"""
Вам доступен текстовый файл, в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, а за ней — непосредственно перечисление козлов разных цветов. Перечень козлов включает только те цвета, которые содержатся в строках из первого списка.

Напишите функцию fresco_goats(), которая принимает название файла, создает файл answer.txt и выводит в него цвета всех козлов, которые удовлетворяют условию загадки от Жака Фреско для указанного файла. Названия цветов козлов следует выводить в алфавитном порядке, каждое на отдельной строке.
"""
def fresco_goats(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    colours = []
    goats = []
    i = 0

    while i < len(lines) and lines[i].strip() != 'COLOURS':
        i += 1
    i += 1

    while i < len(lines) and lines[i].strip() != 'GOATS':
        if lines[i].strip():
            colours.append(lines[i].strip())
        i += 1
    i += 1

    while i < len(lines):
        if lines[i].strip():
            goats.append(lines[i].strip())
        i += 1

    total_goats = len(goats)

    from collections import Counter
    from decimal import Decimal
    goat_counts = Counter(goats)

    result = [
        colour for colour in colours if goat_counts.get(colour, 0) / Decimal(total_goats) * 100 > 7
    ]
    result.sort()

    with open('answer.txt', 'w', encoding='utf-8') as output_file:
        for colour in result:
            output_file.write(colour + '\n')

fresco_goats('goats1.txt')
with open('answer.txt') as f:
   print(f.read())