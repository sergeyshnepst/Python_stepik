import random


# Блок функций
# Проверка ввода числа от пользователя
def is_valid(input_string):
    return input_string.isdigit() and 1 <= int(input_string) <= 100

def input_num():
    while True:
        user_num = input()
        if is_valid(user_num):
            return int(user_num)
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")

# Сравнение введенного пользователем числа и загадонного
def compare_num():
    while True:
        user_num = input_num()
        if user_num > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif user_num < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        else:
            return print("Вы угадали, поздравляем!")  # \nКоличетсво попыток: {count}"


# Основаная программа
num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку\n")
print("Введите число от 1 до 100 включительно")

compare_num()


# count = 1


#    count += 1


# def random_number(fromm, to):
#    num = random.randint(fromm, to)


# пока не предумал как встроить через функцию
# количество попыток для угадывания == 7
def number_of_attempts():
    middle = (left + right) // 2
    count = 1
    while middle != num:
        if middle < num:
            print("мало")
            left = middle + 1
            middle = (left + right) // 2
        elif middle > num:
            print("много")
            right = middle - 1
            middle = (left + right) // 2
        num = int(input())
        count += 1
    print("Угадали", num)
    print(count)


# print(random_number(left, right))
