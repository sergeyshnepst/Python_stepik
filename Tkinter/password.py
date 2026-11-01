from tkinter import *

root = Tk()
root.title("Проверка пароля")
root.geometry("300x200")
password = "SecrEt"


def get_lbl():
    if e.get() == password:
        lbl_get.config(text=f"Доступ разрешен", fg="green")
    else:
        lbl_get.config(text="Неверный пароль", fg="red")


lbl = Label(root, text="Введите текст:")
lbl.pack(pady=5)

e = Entry(root, show="*")
e.pack(pady=5)

btn_get = Button(root, text="Войти", command=get_lbl)
btn_get.pack(pady=5)

lbl_get = Label(root)
lbl_get.pack(pady=5)

root.mainloop()
