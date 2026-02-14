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
sign = ""

def caesar_cipher():
    for x in range(start, qty_output + 1): # Вывод дешифровки в зав известен шаг или нет
        new_text = ""
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].upper():
                    for j in range(n):
                        if text[i] == language[j].upper():
                            new_text += language[(j + x) % n].upper()
                            break
                elif text[i] == text[i].lower():
                    for k in range(n):
                        if text[i] == language[k].lower():
                            new_text += language[(k + x) % n].lower()
                            break
            else:
                new_text += text[i]
    #return new_text
        print(new_text)

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
    language = input("\nНа каком языке шифр?\n")
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
if direction == "dec":
    while True:
        step = input("\nШаг известен?\n")
        if step.lower() == "нет":
            start = 1
            qty_output = n
            break
        elif step.lower() == "да":
            while True:
                step = input("\nКакой шаг выбрать?\n")
                if step.isdigit():
                    start = -int(step)
                    qty_output = -int(step)
                    break
                else:
                    print("Можно ввести только число")
            break
        else:
            print("Можно ввести только 'да' или 'нет'")
elif direction == "enc":
    while True:
        step = input("\nКакой шаг выбрать?\n")
        if step.isdigit():
            start = int(step)
            qty_output = int(step)
            break
        else:
            print("Можно ввести только число")

# Предложение ввести текст
if direction == "dec":
    # step = -int(step)  # подставновка знака "-" в формулу перед шагом
    input_text = "расшифровки"
elif direction == "enc":
    input_text = "шифровки"
text = input(f"\nВведите текст для {input_text}\n")

# Вывод результата
caesar_cipher()
