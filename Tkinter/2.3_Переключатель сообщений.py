from tkinter import *

root = Tk()
root.title('Переключатель сообщений')
root.geometry('300x200+200+200') 

def label_status():
    if current_stage.get() == 'Привет':
        current_stage.set("Пока")
    else:
        current_stage.set("Привет")
    return l.config(text=current_stage.get())


current_stage = StringVar()
current_stage.set('Привет')
l = Label(root, text=current_stage.get())
l.pack(pady=20)

b = Button(root, text="Нажми", command=label_status)
b.pack()

root.mainloop()