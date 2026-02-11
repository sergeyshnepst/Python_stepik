en_alphabet = "abcdefghijklmnopqrstuvwxyz"
ru_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
n = 32
new_text = ""
step = "3"


text = input("\nВведите текст\n")
for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].upper():
                        for j in range(n):
                            if text[i] == ru_alphabet[j].upper():
                                new_text += ru_alphabet[(j + int(step)) % n].upper()
                                break
                    elif text[i] == text[i].lower():
                        for k in range(n):
                            if text[i] == ru_alphabet[k].lower():
                                new_text += ru_alphabet[(k + int(step)) % n].lower()
                                break
                else:
                    new_text += text[i]
print(new_text)
