"""
Вам доступен текстовый файл, содержащий слова, разделенные пробелами. Напишите программу, которая выводит самые длинные слова этого файла, не меняя порядка их следования.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести самые длинные слова указанного файла, каждое на новой строке, не меняя порядка их следования.
"""

with open(input(), 'r', encoding='utf-8') as file:
    lines = file.readlines()
    result = []
    for line in lines:
        words = line.strip().split()
        for word in words:
            result.append(word)
    if result:
        max_length = max(len(word) for word in result)
        longest_words = [word for word in result if len(word) == max_length]
        for word in longest_words:
            print(word)
