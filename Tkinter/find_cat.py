from tkinter import *
from tkinter import messagebox
from random import *

root = Tk()
root.title("Найди кота")
root.geometry("300x200")


def start_game():
    counter = 0
    lbl.config(text=f"Попытки: {counter}")

    for wndw in windows:
        wndw.destroy()
    windows.clear()

    cat_window_index = randint(0, 4)

    for i in range(5):
        wndw = Toplevel(root)
        wndw.geometry("450x150")
        wndw.title(f"Окно {(i + 1)}")

        color = choice(colors)
        wndw.config(bg=color)

        if i == cat_window_index:
            cat_label = Label(
                    wndw,
                    text="🐱 Кот!",
                    font=("Arial", 14, "bold"),
                    bg=color
                )
            cat_label.pack(expand=True)

            wndw.bind()
        else:
            check_btn = Button(
                 wndw,
                 text="Посмотри здесь",
                 command=lambda: check_empty_window(wndw)
            )
            check_btn.pack()

        windows.append(wndw)

def check_empty_window(wndw):
        """Закрывает пустое окно и увеличивает счётчик попыток."""
        wndw.destroy()
        global counter
        counter += 1
        lbl.config(text=f"Попытки: {counter}")

def cat_found():
        """Обрабатывает нахождение кота: показывает сообщение о победе."""
        messagebox.showinfo(
            "Победа!",
            f"Поздравляем! Вы нашли кота за {counter + 1} попыток!"
        )
        # Закрываем все окна, кроме главного
        for wndw in windows:
            wndw.destroy()
        windows.clear()



Button(root, text="Начать игру", height=2, width=10, command=start_game).pack(pady=10)
counter = 0
cat_found = False
windows = []
colors = ["lightblue", "lightgreen", "lightyellow", "lightpink", "lavender"]
lbl = Label(root, text=f"Попытки: {counter}")
lbl.pack(pady=5)

root.mainloop()
