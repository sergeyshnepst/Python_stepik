import random

# Генерация пароля нужной длины
def generate_password(length, chars):
    password = ""
    for j in range(length):
        password += random.choice(chars)
    return password


# Блок основаной программы
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
symbols = "il1Lo0O"
chars = ""

# Количество паролей для генерации;
while True:
    qty_pass = input("\nСколько паролей нужно сгененировать?\n")
    if qty_pass.isdigit():
        break
    else:
        print("Можно ввести только число")

# Длину одного пароля;
while True:
    len_pass = input("\nКакой длины (сколько символов) должен быть пароль?\n")
    if len_pass.isdigit():
        break
    else:
        print("Можно ввести только число")

# Включать ли цифры 0123456789?
while True:
    answer = input("\nВключить цифры в пароль? 'да' или 'нет'\n")
    if answer.lower() == "да":
        chars += digits
        break
    elif answer.lower() == "нет":
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")

# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
while True:
    answer = input("\nВключить прописные буквы в пароль? 'да' или 'нет'\n")
    if answer.lower() == "да":
        chars += uppercase_letters
        break
    elif answer.lower() == "нет":
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")

# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
while True:
    answer = input("\nВключить строчные буквы в пароль? 'да' или 'нет'\n")
    if answer.lower() == "да":
        chars += lowercase_letters
        break
    elif answer.lower() == "нет":
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")

# Включать ли символы !#$%&*+-=?@^_?
while True:
    answer = input("\nВключить спецсимволы в пароль? 'да' или 'нет'\n")
    if answer.lower() == "да":
        chars += punctuation
        break
    elif answer.lower() == "нет":
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")

# Исключать ли неоднозначные символы il1Lo0O?
while True:
    answer = input("\nИсключить неоднознанчее символы 'il1Lo0O'?\n")
    if answer.lower() == "да":
        for i in symbols:
            chars = chars.replace(i, "")
        break
    elif answer.lower() == "нет":
        chars
        break
    else:
        print("Можно ввести только 'да' или 'нет' без кавычек")


for i in range(int(qty_pass)):
    print(f"Ваш пароль {(i + 1)}: {(generate_password(int(len_pass), chars))}\n")
