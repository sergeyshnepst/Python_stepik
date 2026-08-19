"""
Вам доступен список numbers. Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 
2
2 десятичных знаков, а затем выводит их, каждый на отдельной строке.
"""
def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result

def func(x):
    return round(x,2)

numbers = [4.12, 1.3257, 9.37037, 4.552, 3.186]

round_number = map(func, numbers)
print(*round_number, sep='\n')