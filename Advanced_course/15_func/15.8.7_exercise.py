"""
Напишите функцию is_non_negative_num(), используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является неотрицательным числом (целым или вещественным), или False в противном случае.
"""
is_non_negative_num = lambda x: x.replace('.', "").isdigit() and '-' not in x and x.count('.') < 2

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))

