"""
Вам доступен текстовый файл с названиями стран и численностью их населения, разделенными символом табуляции \t.

Напишите программу, которая принимает на вход название текстового файла и выводит все страны, чье название начинается с буквы G, а численность населения больше чем 500000 человек, не меняя их порядок.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести названия стран, удовлетворяющих условиям задачи, каждое на отдельной строке.
"""
with open(input(), 'r', encoding='utf-8') as file:
    lines_list = file.readlines()
    country_list = []
    result = []
    for line in lines_list:
        country_list.append(line.strip().split('\t'))
    for el in country_list:
        if el[0][0] == 'G' and int((country_list[0][1])) >= 500000:
            result.append(el[:len(el)-1])
    for country in result:
        print(''.join(country))

# Решение преподавателя

#with open(input(), 'r', encoding='utf-8') as file:
#    lines_list = file.readlines()
#    country_list = []
#    result = []
#    for line in lines_list:
#        country_list.append(line.strip().split('\t'))
#    for el in country_list:
#       if el[0][0] == 'G' and int((country_list[0][1])) >= 500000:
#            result.append(el[:len(el)-1])
#    for country in result:
#        print(''.join(country))


    
