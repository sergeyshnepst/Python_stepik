"""
Вам доступен список numbers. Напишите программу для вычисления и вывода суммы квадратов двузначных чисел из списка numbers, которые делятся на 
7 без остатка.
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
    return x**2

def func_filter(num):
    return (-100 < num < -10 or 10 < num < 100) and num % 7 == 0

numbers = [14, 15, -1, 2, 0, -42, 36, 2]

filter_numbers = filter(func_filter, numbers)
map_number = map(func, filter_numbers)
print(sum(map_number))