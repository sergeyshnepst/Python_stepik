# Преобразование иконки из формата png в формат ico
from PIL import Image
filen = r'C:\Users\smith\Downloads\free-icon-key-6676705.png'
img = Image.open(filen)
img.save(r'C:\Users\smith\Downloads\icon_key.ico', format = 'ICO', sizes=[(32,32)])