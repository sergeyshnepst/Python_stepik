# y=(x+k) % n для расшифровки
# x=(y−k) % n для шифровки
# где
# x — символ открытого текста,
# y — символ шифрованного текста,
# n — мощность алфавита (количество символов), а
# k — ключ

# Основная программа
en_alphabet = "abcdefghijklmnopqrstuvwxyz"
ru_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
n = 0

def caesar_cipher():
    new_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i] == text[i].upper():
                for j in range(n):
                    if text[i] == language[j].upper():
                        new_text += language[(j + int(step)) % n].upper()
                        break
            elif text[i] == text[i].lower():
                for k in range(n):
                    if text[i] == language[k].lower():
                        new_text += language[(k + int(step)) % n].lower()
                        break
        else:
            new_text += text[i]
    return new_text

# направление: шифрование или дешифрование
while True:
    direction = input("Вы ходите зашифровать или расшифровать текст?\n")
    if direction.lower() == "расшифровать":
        direction = "dec"
        break
    elif direction.lower() == "зашифровать":
        direction = "enc"
        break
    else:
        print("\nМожно ввести только 'расшифровать' или 'дешифровать' без кавычек")

# язык алфавита: русский или английский
while True:
    language = input("На каком языке шифр?\n")
    if language.lower() == "русский" or language.lower() == "ru":
        n = 32
        language = ru_alphabet
        break
    elif language.lower() == "английский" or language.lower() == "eng":
        n = 26
        language = en_alphabet
        break
    else:
        print("Можно ввести только 'русский' или 'английский' без кавычек")

# шаг сдвига (со сдвигом вправо)
while True:
    step = input("\nКакой шаг выбрать?\n")
    if step.isdigit():
        break
    else:
        print("Можно ввести только число")

# Предложение ввести текст
if direction == "dec":
    step = - int(step) # подставновка знака "-" в формулу перед шагом
    input_text = "расшифровки"
elif direction == "enc":
    input_text = "шифровки"
text = input(f"\nВведите текст для {input_text}\n")

# Вывод результата
print(caesar_cipher())