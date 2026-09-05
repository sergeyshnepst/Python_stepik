"""
Вам доступны текстовые файлы, содержащие либо имена, либо фамилии. В файлах каждое имя или фамилия расположены на отдельной строке.

Напишите функцию generate_name(), которая принимает два текстовых файла (первый – с именами, второй – с фамилиями), c помощью модуля random создает случайную пару <имя> <фамилия>, а затем возвращает ее в виде строки.

Примечание 1. Вызывать функцию generate_name() не нужно, требуется только реализовать ее.
"""
from random import choice
def generate_name(first_name, last_name):
    with open(first_name, 'r', encoding='utf-8') as f_name:
        f_list = f_name.readlines()
        random_f_name = choice([line.strip() for line in f_list])
    
    with open(last_name, 'r', encoding='utf-8') as l_name:
        l_list = l_name.readlines()
        random_l_name = choice([line.strip() for line in l_list])
    return f'{random_f_name} {random_l_name}'