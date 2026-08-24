"""
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.
"""
import string as st
password = input()
result = all(
    [len(password) >= 7,
     any(x for x in password if x in st.digits),
     any(x for x in password if x in st.ascii_lowercase),
     any(x for x in password if x in st.ascii_uppercase)
    ]
)
print('YES' if result else 'NO')
