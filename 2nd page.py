from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("Sign-in")
window.geometry('630x420')
window.resizable(False,False)
window.config(bg="#0a3570")
image = Image.open("page2.png")
resize_image = image.resize((650,420))
img1 = ImageTk.PhotoImage(file="page2.png")
my_canvas=Canvas(window,width=650,height=420,bg="#0a3570")
my_canvas.create_image(0,0,image=img1,anchor=NW)
my_canvas.pack(fill="both",expand=True)
img2 = ImageTk.PhotoImage(Image.open("output-onlinepngtools (1).png"))
dashboard_btn=Button(window,text="DASHBOARD",font=("comic sans",18,"normal","underline"),
                     bg="#fabd75",fg="#807772",border=0,activebackground="#fabd75",activeforeground="#807772")
dashboard_btn.place(x=109,y=170)
product_btn=Button(window,text="PRODUCT",font=("comic sans",18,"normal","underline"),
                   bg="#fabd75",fg="#807772",border=0,activebackground="#fabd75",activeforeground="#807772")
product_btn.place(x=423,y=170)
low_stock_btn=Button(window,text="LOW STOCK",font=("comic sans",18,"normal","underline"),
                     bg="#fabd75",fg="#807772",border=0,activebackground="#fabd75",activeforeground="#807772")
low_stock_btn.place(x=111,y=277)
transactions_btn=Button(window,text="TRANSACTION",font=("comic sans",18,"normal","underline"),
                        bg="#fabd75",fg="#807772",border=0,activebackground="#fabd75",activeforeground="#807772")
transactions_btn.place(x=398,y=277)
b2 = Button(window, image=img2,border=0)
b2.place(x=10, y=8)
window.mainloop()