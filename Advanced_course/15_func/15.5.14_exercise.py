"""
Напишите функцию func_apply(), принимающую функцию и список значений и возвращающую список, в котором каждое значение будет результатом применения переданной функции к переданному списку.
"""
def func_apply(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result

print(func_apply(int, ['1', '2', '10']))
print(func_apply(bool, [1, 2, 3, 4, 5, 0]))