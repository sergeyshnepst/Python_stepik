from tkinter import *

root = Tk()
root.title("Очиститель")
root.geometry("300x200")
password = "SecrEt"


def show_text():
    lbl_get["text"] = e.get()


def clear_text():
    e.delete(0, END)


def reset_text():
    e.insert(0, lbl_get["text"])


lbl = Label(root, text="Введите текст:")
lbl.pack(pady=5)

e = Entry(root)
e.insert(0, "Тестовый текст")
e.pack(pady=5)

btn_show = Button(root, text="Показать", command=show_text)
btn_show.pack(pady=5)

btn_clear = Button(root, text="Очистить", command=clear_text)
btn_clear.pack(pady=5)

# Добавь кнопку «Восстановить», которая вставляет обратно последний показанный текст
btn_reset = Button(root, text="Восстановить", command=reset_text)
btn_reset.pack(pady=5)

lbl_get = Label(root)
lbl_get.pack(pady=5)

root.mainloop()
