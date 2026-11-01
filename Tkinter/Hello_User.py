from tkinter import *

root = Tk()
root.title("Приветствие")
root.geometry("350x200")


def get_lbl():
    if e.get() != "":
        lbl_get.config(text=f"Привет, {e.get()}!")
    else:
        lbl_get.config(text="Привет, незнакомец!")


lbl = Label(root, text="Введите Ваше имя:")
lbl.pack(pady=5)

e = Entry(root)
e.pack(pady=5)

btn_get = Button(root, text="Поздороваться", command=get_lbl)
btn_get.pack(pady=5)

lbl_get = Label(root)
lbl_get.pack(pady=5)

root.mainloop()
