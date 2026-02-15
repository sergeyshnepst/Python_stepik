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
print(lst)