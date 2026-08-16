"""
Напишите функцию greet(), которая принимает произвольное количество строк-имен (как минимум одну) и возвращает приветствие в соответствии с тестовыми данными.

Примечание 1. Обратите внимание: функция должна принимать не список, а именно произвольное количество аргументов.
"""

def greet(name, *args):
    if len(args) > 0:
        return f"Hello, {name} and {' and '.join(args)}!"
    else:
        return f"Hello, {name}!"    

print(greet('Timur'))
print(greet('Timur', 'Roman', 'Ruslan'))

#вариант проще
'''
def greet(*args):
        return f"Hello {' and '.join(args)}!"
'''