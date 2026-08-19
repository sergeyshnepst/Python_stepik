"""
Вам доступен список numbers. Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers.
"""
# 1ый вариант через reduce()
'''
def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item**2)
    return acc
   
def add(x,y):
    return x+y

numbers = [7, 5, -4, 0, 3, -5, 6, 7, 15]
result_list = reduce(add, numbers, 0)
print(result_list)
'''
# 2ой вариант через map() + sum()
def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result

def quart(x):
    return x**2

numbers = [7, 5, -4, 0, 3, -5, 6, 7, 15]
total = map(quart, numbers)
print(sum(total))