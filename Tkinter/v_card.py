from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Визитка")

lbl = Label(
    root,
    text="Иван Васильевич\nПетров\nСтудент\nМосква",
    bg="grey",
    fg="yellow",
    font=("Arial", 14, "bold"),
    justify=CENTER,
    anchor=CENTER,
    relief="ridge",
    padx=10,
    pady=10,
)
lbl.pack(expand=True)

root.mainloop()
