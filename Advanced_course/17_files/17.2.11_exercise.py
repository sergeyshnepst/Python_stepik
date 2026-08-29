"""
Напишите программу, которая принимает на вход строку с именем текстового файла и выводит содержимое этого файла.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести содержимое указанного файла.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Не забудьте закрыть файл.

There are more insects on the earth than all other kinds of animals.
Insects live everywhere – in the garden, in the pond, in the forests, and even in deserts.
Some insects live in the oceans or in very cold places, such as Antarctica.
"""
file = open(input(), 'r', encoding='utf-8')

animals = file.read()
print(animals.strip())

file.close()
