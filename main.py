from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
window=Tk()
window.title("Sign-in")
window.geometry('600x420')
window.resizable(False,False)
window.config(bg="#0a3570")
# image1 = Image.open("Ayush prototype.png")
# resize_image = image1.resize((600,420),Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(file="Ayush prototype.png")
# image1.close()
# label=Label(window,image=img,bd=0).place(x=20,y=30)
# frame=Frame(window,width=300,height=300,bg="#eec4c9").place(x=350,y=30)
# username_icon=PhotoImage(file="username icon.png")
my_canvas=Canvas(window,width=600,height=420,bg="#0a3570",highlightthickness=0,borderwidth=0)
my_canvas.create_image(0,0,image=img1,anchor=NW)
# my_canvas.create_text(300, 50, text="Dont have an account? Sign-up", fill="#d3b072", font=('Helvetica 15 bold'))
my_canvas.pack(fill="both",expand=True)
sign_up=Label(window,text="Dont have an account? Sign-up",fg="#d3b072",font=("comic sans",10),bg="#0a3570")
sign_up.place(x=380,y=320)
username_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
username_entry.insert(0,"username")
username_entry.place(x=433,y=116)
password_entry =Entry(window,bd=0, width=9,font=('comic sans', 17, 'normal'),bg="#ffffff")
password_entry.insert(0,"password")
password_entry.place(x=431,y=185)
log_in=Button(window,text="SIGN-IN",bd=0,font=("comic sans",17,"bold","underline"),bg="#ffbd59",width=11,
              fg="#0a3570",activeforeground="#0a3570",activebackground="#ffbd59")
log_in.place(x=390,y=253)



window.mainloop()