"""
Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой.

Функция должна получать на вход один обязательный аргумент data – список, который следует вывести и два необязательных строковых односимвольных  аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует аргумент delimiter, то полагаем delimiter='|'.

Примечание. Считайте, что side и delimiter состоят всегда из одного символа.
"""
def pretty_print(data, side='-', delimiter='|'):
    a = []
    for d in range(len(data)):
        a.append(delimiter + " " + str(data[d]))
    b = []
    c = " ".join(a) + " " + delimiter
    b.append(" " + side*(len(c)-2) + " ")
    b.append(c)
    b.append(" " + side*(len(c)-2) + " ")
    print("\n".join(b))

pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
