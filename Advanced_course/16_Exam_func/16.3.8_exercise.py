"""
Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций (+, -, *, /) и возвращает функцию двух аргументов для соответствующей операции.

Примечание 1. Вызывать функцию arithmetic_operation() не нужно, требуется только реализовать ее.

Примечание 2. Модуль operator может быть полезен при решении этой задачи.
"""
import operator
d = {"+" : operator.add,
       "-" : operator.sub,
       "*" : operator.mul,
       "/" : operator.truediv}
def arithmetic_operation(symbol):
    return lambda x, y: d[symbol](x, y)

div = arithmetic_operation('/')
print(div(20, 5))