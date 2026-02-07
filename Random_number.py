import random
# Блок функций
# выбор числа для правой границы
def choise_right_limit():
    while True:
        right_limit = input("Выберите в каком диапазоне загадать число компьютеру, от 1 до?\n")
        if right_limit == "q":
            exit()
        elif right_limit.isdigit():
            return int(right_limit)
        else:
            print('Можно ввести только целое число')

# Проверка ввода числа от пользователя
def is_valid(input_string):
    return input_string.isdigit() and 1 <= int(input_string) <= right_limit

def input_num():
    while True:
        user_num = input()
        if user_num.lower() == 'q':
            exit()
        elif is_valid(user_num):
            return int(user_num)
        else:
            print(f"А может быть все-таки введем целое число от 1 до {right_limit}?")

# Сравнение введенного пользователем числа и загадонного
def compare_num():
    count = 1
    while True:
        user_num = input_num()
        count += 1
        if user_num > num:
            print("Ваше число больше загаданного, попробуйте еще разок\n")
        elif user_num < num:
            print("Ваше число меньше загаданного, попробуйте еще разок\n")
        else:
            return print(f"Вы угадали, поздравляем!\nКоличетсво попыток: {count}")

# Предложение сыграть еще раз
def play_again(): 
    print("Хотите сыграть еще раз?\nОтвет \"y\" или \"n\"")
    while True:
        play_again = input()
        if play_again == "q":
            exit()
        elif play_again.lower() == "y":
            return True
        elif play_again.lower() == "n":
            print('Спасибо, запустите программу еще раз, если захотите поиграть в \"Угадайку\"')
            break
        else:
            print('Можно ввести только \"y\" или \"n\" без кавычек')

# Основаная программа
print("Добро пожаловать в числовую угадайку\n")
print("Компьютер загадает число, а вы должны его отгадать за минимальное количество попыток")
print('Если захотите выйти введите \"q\" без кавычек')
while True:
    right_limit = choise_right_limit()
    num = random.randint(1, right_limit + 1)
    print(f"\nВведите число от 1 до {right_limit} включительно:")
    compare_num()
    if not play_again():
        break