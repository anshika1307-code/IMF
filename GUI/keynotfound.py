from tkinter import *
from PIL import Image, ImageTk
import os



def close():
    wlc.destroy()
    os.system('python adddatabase.py')

wlc=Tk()
wlc.geometry('1000x700+200+30')
wlc.title('Key Not Found')
bgwlc = PhotoImage(file='notfound.png')
bgwlcLabel = Label(wlc, image=bgwlc)
bgwlcLabel.place(x=0, y=0)
bgwlcLabel.pack()

wlcframe2 = Frame(wlc, bg='white', width=140, height=100)
wlcframe2.place(x=900, y=120)

proceedimage2=Image.open("close.png")
resized2=proceedimage2.resize((20,20),Image.ANTIALIAS)
new_image2=ImageTk.PhotoImage(resized2)
proceedbutton2 = Button(wlcframe2, image=new_image2, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white',command=close)
proceedbutton2.place(x=900, y=120)
proceedbutton2.pack()

wlc.mainloop()



