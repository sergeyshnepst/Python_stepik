en_alphabet = "abcdefghijklmnopqrstuvwxyz"

string = input()
lst = []
st = ""
# преобразование строки в список со знакоми препинания и пробелами
# ['Day', ',', ' ', 'mice', '.', ' ', '"', 'Year', '"', ' ', 'is', ' ', 'a', ' ', 'mistake', '!']
for sym in string:
    if sym.isalpha():
        st += sym
    else:
        if len(st):
            lst.append(st)
        lst.append(sym)
        st = ""
# добавление последнего слова в список, если нет знаков припинания в конце строки
if len(st):
    lst.append(st)

new_text = []
n = 26  # количество символов в алфавите

# Основная программа
for element in lst:
    for i in range(len(element)):
        if element[i].isalpha():
            if element[i] == element[i].upper():
                for j in range(n):
                    if element[i] == en_alphabet[j].upper():
                        new_text += en_alphabet[(j + len(element)) % n].upper()
                        # break
            elif element[i] == element[i].lower():
                for j in range(n):
                    if element[i] == en_alphabet[j].lower():
                        new_text += en_alphabet[(j + len(element)) % n].lower()
                        # break
        else:
            new_text.append(element[i])
print("".join(new_text))
