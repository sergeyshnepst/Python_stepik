from tkinter import *


def ask_question():
    dialog = Toplevel(root)
    dialog.title("Вопрос")
    dialog.geometry("250x120")
    dialog.transient(root)  # привязано к главному
    dialog.grab_set()  # модальный режим
    dialog.focus_set()

    Label(dialog, text="Вы любите Python?").pack(pady=10)

    def answer(choice):
        print("Ответ:", choice)
        dialog.destroy()

    Button(dialog, text="Да", command=lambda: answer("Да")).pack(side=LEFT, padx=20)
    Button(dialog, text="Нет", command=lambda: answer("Нет")).pack(side=RIGHT, padx=20)

    # Запрещаем закрытие через крестик без выбора
    dialog.protocol("WM_DELETE_WINDOW", lambda: None)


root = Tk()
root.geometry("300x200")
Button(root, text="Задать вопрос", command=ask_question).pack(pady=50)
root.mainloop()
