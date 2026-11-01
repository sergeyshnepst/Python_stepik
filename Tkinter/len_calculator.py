from tkinter import *

root = Tk()
root.title("Калькулятор длины")
root.geometry("300x200")


def get_lbl():
    lbl_get.config(text=f"Длина: {(len(e.get()))} символов!")


lbl = Label(root, text="Введите текст:")
lbl.pack(pady=5)

e = Entry(root)
e.pack(pady=5)

btn_get = Button(root, text="Посчитать длину", command=get_lbl)
btn_get.pack(pady=5)

lbl_get = Label(root)
lbl_get.pack(pady=5)

root.mainloop()
