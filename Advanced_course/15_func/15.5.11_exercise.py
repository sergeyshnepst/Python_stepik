"""
Вам доступен список numbers. Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трехзначные числа, дающие при делении на 5 остаток 2, и выводит их кубы, каждый на отдельной строке.
"""
def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result

def filter(function, items):
    result = []
    for item in items:
        if function(item):        
            result.append(item)  # добавляем элемент item если функция function вернула значение True
    return result

def func(x):
    return x**3

def func_filter(x):
    return len(str(x)) == 3 and x % 5 == 2

numbers = [854, 10, 5, 452, 478, 236, 202, 41]
filter_numbers = filter(func_filter, numbers)
map_number = map(func, filter_numbers)
print(*map_number, sep='\n')