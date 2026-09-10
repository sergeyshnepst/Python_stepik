"""
Напишите функцию write_random_numbers(), которая принимает целое число n и записывает в текстовый файл random.txt n случайных целых чисел в диапазоне от 111 до 777 (включительно), каждое на отдельной строке.
"""
def write_random_numbers(number):
    with open('random.txt', 'w', encoding='utf-8') as output_file:
        for _ in range(number):
            import random
            print(random.randint(111, 777), file=output_file)

write_random_numbers(4)
with open('random.txt') as f:
    print(f.read())