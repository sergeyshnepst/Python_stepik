from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Демонстрация Label")
root.geometry("400x500")

# 1. Простая текстовая метка
lbl1 = Label(root, text="Обычный текст", bg="lightblue")
lbl1.pack(pady=5)

# 2. Текст с настройками
lbl2 = Label(
    root,
    text="Жирный шрифт\nи несколько строк",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="darkgreen",
    justify=CENTER,
    width=25,
    height=3,
    relief="raised",
)
lbl2.pack(pady=5)

# 3. Картинка
try:
    img = Image.open(r"C:\Users\smith\Desktop\Python\TKInter\homer.gif")
    img = img.resize((80, 80))
    photo = ImageTk.PhotoImage(img)
    lbl3 = Label(root, image=photo)
    lbl3.pack(pady=5)
    # сохраняем ссылку, чтобы не удалилось
    lbl3.image = photo
except:
    lbl3 = Label(root, text="(картинка не найдена)")
    lbl3.pack(pady=5)

# 4. Текст + картинка
try:
    photo2 = ImageTk.PhotoImage(Image.open(r"C:\Users\smith\Desktop\Python\TKInter\homer.gif").resize((40, 40)))
    lbl4 = Label(
        root,
        text="Python",
        image=photo2,
        compound=LEFT,
        font=("Arial", 18),
        bg="yellow",
    )
    lbl4.pack(pady=5)
    lbl4.image = photo2
except:
    pass

root.mainloop()
