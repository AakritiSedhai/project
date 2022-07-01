from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("Sign-in")
window.geometry('650x420')
window.resizable(False,False)
window.config(bg="#0a3570")
image = Image.open("page2.png")
resize_image = image.resize((500,420))
img1 = ImageTk.PhotoImage(file="page2.png")
my_canvas=Canvas(window,width=200,height=200,bg="#0a3570")
my_canvas.create_image(10,10,image=img1,anchor=NW)
my_canvas.pack(fill="both",expand=True)

window.mainloop()