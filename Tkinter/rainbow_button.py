from tkinter import *

root = Tk()
root.title("Цвета радуги")
root.geometry("300x200")
rainbow_colors = ["red", "orange", "yellow", "green", "light blue", "blue", "indigo"]
rainbow_colors_ru = [
    "красный",
    "оранжевый",
    "желтый",
    "зеленый",
    "голубой",
    "синий",
    "фиолетовый",
]
color = 0


def click_change_color():
    global color
    root.config(bg=rainbow_colors[color])
    if color > 5:
        color = 0
    else:
        color += 1
    btn.config(text=f"Сменить цвет на {(rainbow_colors_ru[color])}")


btn = Button(
    root,
    text=f"Сменить цвет, на {rainbow_colors_ru[0]}",
    bg="white",
    command=click_change_color,
)

btn.pack(expand=True)

root.mainloop()
