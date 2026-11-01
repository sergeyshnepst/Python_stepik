from tkinter import *

root = Tk()
root.title("Три кнопки")
root.geometry("300x200")


def click_change_color(color):
    root.config(bg=color)
    return color


# Использование Лямбда функции для срабатывание параметра функции.
# Без лямбда получилось запустить только тремя отдельными функциями
btn_red = Button(root, bg="red", command=lambda: click_change_color("red"))
btn_green = Button(root, bg="green", command=lambda: click_change_color("green"))
btn_blue = Button(root, bg="blue", command=lambda: click_change_color("blue"))
btn_red.pack()
btn_green.pack()
btn_blue.pack()

root.mainloop()
