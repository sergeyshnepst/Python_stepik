import random


def generate_password(chars):
    return random.choice(chars)


# Блок основаной программы
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
symbols = "il1Lo0O"
chars = ""
password = ""

# Количество паролей для генерации;
qty_pass = input("Сколько паролей нужно сгененировать?\n")
while True:
    if not qty_pass.isdigit():
        print("Можно ввести только число")
    else:
        break

# Длину одного пароля;
len_pass = input("Какой длины (сколько символов) должен быть пароль?\n")
while True:
    if not len_pass.isdigit():
        print("Можно ввести только число")
    else:
        break

# Включать ли цифры 0123456789?
while True:
    answer = input(f"Включить цифры в пароль? 'да' или 'нет'\n")
    if answer.lower() == "да":
        chars += digits
        break
    elif answer.lower() == "нет":
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")

# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
while True:
    answer = input(f"Включить прописные буквы в пароль? 'да' или 'нет'\n")
    if answer.lower() == "да":
        chars += uppercase_letters
        break
    elif answer.lower() == "нет":
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")

# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
while True:
    answer = input(f"Включить строчные буквы в пароль? 'да' или 'нет'\n")
    if answer.lower() == "да":
        chars += lowercase_letters
        break
    elif answer.lower() == "нет":
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")

# Включать ли символы !#$%&*+-=?@^_?
while True:
    answer = input(f"Включить спецсимволы в пароль? 'да' или 'нет'\n")
    if answer.lower() == "да":
        chars += punctuation
        break
    elif answer.lower() == "нет":
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")

# Исключать ли неоднозначные символы il1Lo0O?

# Продумать как исключить символы из уже известного набора
result = ""
while True:
    answer = input("Исключить неоднознанчее символы 'il1Lo0O'?\n")
    if answer.lower() == "да":
        for i in symbols:
            if i not in chars:
                result += i
        break
    elif answer.lower() == "нет":
        result = chars
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")


# generate_password(result)


# TODO
# for i in range(qty_pass):

for i in range(int(len_pass)):
    password += generate_password(result)
