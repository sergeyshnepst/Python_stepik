from tkinter import *

root = Tk()
root.title("Конвертер температуры")
root.geometry("350x200")


def conv_to_F():
    try:
        result.config(text=f"{((float(e.get()) * 9) / 5 + 32)} °F")
    except ValueError:
        result.config(text="Ошибка: введите число")


celsius = Label(root, text="Градусы Цельсия")
celsius.pack(pady=5)

e = Entry(root)
e.pack(pady=5)

btn_conv = Button(root, text="Перевести в Фаренгейты", command=conv_to_F)
btn_conv.pack(pady=5)

result = Label(root)
result.pack(pady=5)

root.mainloop()
