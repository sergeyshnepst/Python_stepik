"""
Вам доступен текстовый файл с оценками за итоговый тест, в котором каждая строка записана в следующем формате:

<фамилия> <оценка>
            
где <оценка> – целое число от 0 до 100 (включительно).

Напишите функцию add_five(), которая принимает название файла и добавляет 5 баллов к каждому результату теста и выводит фамилии и новые результаты теста в файл new_scores.txt. Если после добавления 5 баллов новая оценка превышает 100, то она принимается равной 100.
"""
def add_five(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('new_scores.txt', 'w', encoding='utf-8') as output_file:
        for line in lines:
            name, score= line. split()
            newscore = int(score) + 5
            if newscore > 100:
                newscore = 100
            output_file.write(f"{name} {newscore}\n")

add_five('class_scores1.txt')
with open('new_scores.txt') as f:
    print(f.read())