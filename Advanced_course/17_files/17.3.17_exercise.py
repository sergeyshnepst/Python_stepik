"""
Вам доступен CSV-файл, содержащий информацию в csv-формате. Напишите функцию read_csv(), которая принимает название CSV-файла, считывает данные из этого файла и возвращает список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку – как значения этих ключей.

Примечание 1. Гарантируется, что все элементы в CSV-файле разделены запятой.

Примечание 2. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 3. Вызывать функцию read_csv() не нужно, требуется только реализовать ее.

Примечание 4. Все ключи и значения в результирующем словаре должны иметь строковый тип (тип str)
"""
def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        data = []
        result = []
        for line in lines[:1]:
            headers = line.strip().split(",")
        for line in lines[1:]:
            data.append(line.strip().split(","))
        for el in data:
            result.append(dict(zip(headers, el)))
        return result

# Решение проподавателя:
#def read_csv(filename):
#    res = []
#    with open(filename) as f:
#        keys = f.readline().rstrip().split(',')
#        for line in f:
#            values = line.rstrip().split(',')
#            cur_dict = dict(zip(keys, values))
#            res.append(cur_dict)
            
#    return res

    
