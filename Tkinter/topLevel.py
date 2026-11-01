from tkinter import *


def create_window():
    # Создаем дополнительное окно
    new_window = Toplevel()
    new_window.title("Временное окно")
    new_window.geometry("300x200")

    # Добавление кнопки для удаления этого окна
    Button(new_window, text="Закрыть овно", command=new_window.destroy).pack(pady=50)


# Главное окно
root = Tk()
root.title("Главное окно")
root.geometry("350x200")

# Кнопка для открытия окна
Button(root, text="Открыть окно", command=create_window).pack(pady=50)

# Кнопка для закрытия Всех окон
Button(root, text="Закрыть все", command=root.destroy).pack(pady=20)

root.mainloop()
