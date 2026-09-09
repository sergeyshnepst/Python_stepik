"""
Вам доступен CSV-файл, содержащий информацию в csv-формате. Напишите функцию read_csv(), которая принимает название CSV-файла, считывает данные из этого файла и возвращает список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку – как значения этих ключей.

Примечание 1. Гарантируется, что все элементы в CSV-файле разделены запятой.

Примечание 2. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 3. Вызывать функцию read_csv() не нужно, требуется только реализовать ее.

Примечание 4. Все ключи и значения в результирующем словаре должны иметь строковый тип (тип str)
"""
def file_size(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        size = 0
        lines = file.readlines()
        for line in lines:
            for symbol in line:
                if symbol == '\n':
                    size += 2
                else:
                    size += 1
        return filename, size

n = int(input())
d = {}
for num in range(n):
    size, filename = file_size(input())
    d[size] = filename
res = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i in res:
    print(f'{i[0]} {i[1]}B')

