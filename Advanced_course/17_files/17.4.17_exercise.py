"""
Напишите функцию concatenate_files(), которая принимает произвольное количество аргументов-строк с названиями файлов, создает файл output.txt и выводит в него содержимое всех файлов, не меняя их порядка.
"""
def concatenate_files(*filename):
    lines = []
    for name in filename:
        with open(name, 'r', encoding='utf-8') as file:
            lines.extend(file.readlines())
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for line in lines:
            output_file.write(line)

concatenate_files('travelling1.txt', 'travelling2.txt')
with open('output.txt') as f:
    print(f.read())

# Решение преподавателя:
#def concatenate_files(*filenames):
#    data = ''
#    for filename in filenames:
#        with open(filename) as f:
#            data += f.read()
#    
#    with open('output.txt', 'w') as f:
#        f.write(data)