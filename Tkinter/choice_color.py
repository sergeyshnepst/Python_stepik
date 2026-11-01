from tkinter import *

root = Tk()
root.title("Выбор цвета")
root.geometry("300x200")


def click_opn_wndw(color):
    wndw = Toplevel(root)
    wndw.grab_set()
    wndw.geometry("250x150")
    if color:
        wndw.config(bg=color)

    Label(wndw, text=f"Вы выбрали {color}!").pack(pady=50)
    Button(wndw, text="Назад", command=wndw.destroy).pack(pady=5)


Button(root, bg="red", height=3, width=10, command=lambda: click_opn_wndw("red")).pack()
Button(
    root, bg="blue", height=3, width=10, command=lambda: click_opn_wndw("blue")
).pack()
Button(
    root, bg="green", height=3, width=10, command=lambda: click_opn_wndw("green")
).pack()

root.mainloop()
