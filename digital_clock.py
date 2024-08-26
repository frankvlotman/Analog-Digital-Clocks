from tkinter import *
from tkinter.ttk import *
from time import strftime
from PIL import Image

# Define the path for the blank icon
icon_path = 'C:\\Users\\Frank\\Desktop\\blank.ico'

# Create a blank (transparent) ICO file if it doesn't exist
def create_blank_ico(path):
    size = (16, 16)  # Size of the icon
    image = Image.new("RGBA", size, (255, 255, 255, 0))  # Transparent image
    image.save(path, format="ICO")

# Create the blank ICO file
create_blank_ico(icon_path)

root = Tk()
root.title('Clock')
root.iconbitmap(icon_path)  # Set the custom icon

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('franklin gothic', 40, 'bold'),
            background='green',
            foreground='gold')
lbl.pack(anchor='center')

time()
mainloop()
