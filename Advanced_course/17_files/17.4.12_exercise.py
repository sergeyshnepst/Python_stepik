"""
Вам доступен текстовый файл, содержащий одну строку. Напишите функцию write_line(), которая принимает название файла, считывает строку текста из указанного файла и записывает ее в файл output.txt.

Примечание 1. Вызывать функцию write_line() не нужно, требуется только реализовать ее.
"""
def write_line(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        line = file.readline()
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(line)
    
write_line('first_program.txt')
with open('output.txt') as f:
    print(f.read())