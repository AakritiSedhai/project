from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
window=Tk()
window.title("Sign-in")
window.geometry('600x420')
window.resizable(False,False)
window.config(bg="#0a3570")
image = Image.open("SIGN-IN.png")
resize_image = image.resize((600,420),Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(file="SIGN-IN.png")
# label=Label(window,image=img,bd=0).place(x=20,y=30)
# frame=Frame(window,width=300,height=300,bg="#eec4c9").place(x=350,y=30)
# username_icon=PhotoImage(file="username icon.png")
my_canvas=Canvas(window,width=500,height=420,bg="#0a3570")
my_canvas.create_image(10,10,image=img1,anchor=NW)
# my_canvas.create_text(300, 50, text="Dont have an account? Sign-up", fill="#d3b072", font=('Helvetica 15 bold'))
my_canvas.pack(fill="both",expand=True)
sign_up=Label(window,text="Dont have an account? Sign-up",fg="#d3b072",font=("comic sans",10),bg="#0a3570")
sign_up.place(x=380,y=320)
username_entry =Entry(window,bd=0, width=10,font=('comic sans', 17, 'normal'),bg="#d9d9d9")
username_entry.insert(0,"username")
username_entry.place(x=435,y=125)
password_entry =Entry(window,bd=0, width=10,font=('comic sans', 17, 'normal'),bg="#d9d9d9")
password_entry.insert(0,"password")
password_entry.place(x=435,y=195)
log_in=Button(window,text="SIGN-IN",bd=0,font=("comic sans",17,"bold","underline"),bg="#b7daef",width=11,fg="#0a3570")
log_in.place(x=400,y=262)



window.mainloop()