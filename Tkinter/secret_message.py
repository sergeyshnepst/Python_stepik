from tkinter import *

root = Tk()
root.title("Секретная база")
root.geometry("300x200")


def check():
    wndw = Toplevel(root)
    wndw.grab_set()
    wndw.geometry("450x150")
    lbl = Label(wndw)
    lbl.pack(pady=50)
    Button(wndw, text="Назад", command=wndw.destroy).pack(pady=5)
    if e.get() == "12345":
        lbl.config(text="Добро пожаловать, агент! Ваше задание: выучить Python!")
    else:
        lbl.config(text="Доступ запрещён!")
    wndw.after(2000, wndw.destroy)


e = Entry(root, show="●")
e.pack(pady=50)

Button(root, text="Войти", height=2, width=10, command=check).pack()

root.mainloop()
