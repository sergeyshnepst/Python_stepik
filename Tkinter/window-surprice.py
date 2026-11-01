from tkinter import *


def new_window():
    dialog = Toplevel(root)
    dialog.title("Сюрприз")
    # dialog.geometry("250x120")
    dialog.transient(root)  # привязано к главному
    dialog.grab_set()  # модальный режим
    dialog.focus_set()

    Label(dialog, text="Ура! Ты создал свое первое дополнительное окно!").pack(pady=10)


root = Tk()
root.title("Моя первая программа")
root.geometry("300x200")
Button(root, text="Сюрприз!", command=new_window).place(
    relx=0.5, rely=0.5, anchor="center"
)
root.mainloop()
