"""
Вам доступен текстовый файл с информацией о времени входа пользователя в систему и выхода из нее. Каждая строка файла записана в следующем формате:

<имя пользователя>, <время входа>, <время выхода>
               
где время указано в формате hh:mm.

Напишите функцию write_long_session_users(), которая принимает название файла с информацией о времени входа пользователя в систему и выхода из нее, создает файл output.txt и выводит в него имена всех пользователей (не меняя порядка следования), которые были в сети не менее часа.
"""
def write_long_session_users(filename):
    with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            result = []
            for line in lines:
                name, start, end = line.strip().split(', ')
                start_hours, start_minutes = map(int, start.split(':'))
                end_hours, end_minutes = map(int, end.split(':'))
                duration = (end_hours * 60 + end_minutes) - (start_hours * 60 + start_minutes)
                if duration >= 60:
                    result.append(name)
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for name in result:
            output_file.write(f"{name}\n")

write_long_session_users('logfile1.txt')
with open('output.txt') as f:
    print(f.read())

