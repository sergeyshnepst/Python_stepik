"""
Вам доступен список mixed_list, содержащий целочисленные и строковые значения. Напишите программу, которая с помощью встроенной функции max() находит и выводит наибольшее числовое значение в указанном списке.
"""
mixed_list = ['cow', 12, 'chicken', 'sand', 75]

result = max(mixed_list, key=lambda avg: avg if isinstance(avg, int) else 0)
print(result)




