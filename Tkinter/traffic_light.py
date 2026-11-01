from tkinter import *

root = Tk()
root.geometry("300x450")
root.title("Traffic light")

red = Label(
    root,
    text="Стой",
    bg="red",
    fg="white",
    width=10,
    height=5,
    font=("Arial", 16, "bold"),
    relief="raised",
)
yellow = Label(
    root,
    text="Внимание",
    bg="yellow",
    fg="black",
    width=10,
    height=5,
    font=("Arial", 16, "bold"),
    relief="raised",
)
green = Label(
    root,
    text="Иди",
    bg="green",
    fg="white",
    width=10,
    height=5,
    font=("Arial", 16, "bold"),
    relief="raised",
)
red.pack(
    side=TOP,
    pady=10,
)
yellow.pack(
    side=TOP,
    pady=10,
)
green.pack(
    side=TOP,
    pady=10,
)

root.mainloop()
