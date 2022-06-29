from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("Sign-in")
window.geometry('600x420')
window.resizable(False,False)
window.config(bg="#0a3570")
image = Image.open("page2.png")
resize_image = image.resize((600,420),Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(file="page2.png")
my_canvas=Canvas(window,width=500,height=420,bg="#0a3570")
my_canvas.create_image(10,10,image=img1,anchor=NW)
my_canvas.pack(fill="both",expand=True)
window.mainloop()