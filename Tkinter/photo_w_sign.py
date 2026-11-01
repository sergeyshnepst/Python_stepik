from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
root.title("Фото с подписью")


img = Image.open(r"C:\Users\smith\Desktop\Python\TKInter\logo_eagle.jpg")
img = img.resize((400, 400))  # меняем размер
photo = ImageTk.PhotoImage(img)
label_img = Label(root, text="Мой логотип", image=photo, compound=TOP, fg="blue",
    font=("BoldItalic", 18),)
label_img.pack()

# Вариант для надписи отдельным лейблом (удалить compound)
#lbl = Label(
#    root,
#    text="Мой логотип",
#    fg="blue",
#    font=("BoldItalic", 18),
#)
#lbl.pack(side=TOP, pady=5)

root.mainloop()
