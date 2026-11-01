from tkinter import *

root = Tk()
root.geometry("600x400+1000+300")


def get_srt():  # создаём функцию, которая передаёт текст из поля на метку
    l_text["text"] = e.get()


e = Entry(root, show="*")  # создаём само поле # все символы будут скрыты *

# e.insert(0, "Hello world")  # записываем в поле текст 'Hello word'
e.pack()

btn_get = Button(
    root, text="Get", command=get_srt
)  # создаём кнопку, которая при нажатии
btn_get.pack()  # передает текст из поля на метку

l_text = Label(root)  # создаём метку, которая будет принимать текст из поля
l_text.pack()

root.mainloop()
